/* Swiss Training Ledger: local-first journal types and persistence helpers for the daily checkpoint workflow. */

export type JapaneseType = "kotoba" | "kanji" | "bunpou";
export type JLPTLevel = "N5" | "N4" | "N3";

export interface JapaneseEntry {
  id: string;
  type: JapaneseType;
  content: string;
  reading: string;
  jlpt: JLPTLevel;
  studyMinutes: number;
  sentence: string;
  sentenceMinutes: number;
}

export interface WorkoutLog {
  ladder: boolean;
  ladderRounds: number;
  ladderMinutes: number;
  ladderNotes: string;
  cindy: boolean;
  cindyRounds: number;
  cindyMinutes: number;
  cindyNotes: string;
}

export interface DailyLog {
  date: string;
  workout: WorkoutLog;
  japanese: JapaneseEntry[];
  freeMinutes: number;
  note: string;
  updatedAt: string;
}

export interface TrackerStore {
  version: 1;
  logs: Record<string, DailyLog>;
  lastSyncedAt?: string;
}

const STORAGE_KEY = "gateway-tracker-v1";
const MAX_RANGE_DAYS = 3660;
const DATE_KEY = /^\d{4}-\d{2}-\d{2}$/;

const safeMinutes = (value: unknown) => {
  const numeric = Number(value);
  return Number.isFinite(numeric) ? Math.max(0, Math.min(1440, Math.round(numeric))) : 0;
};

const safeText = (value: unknown, limit = 1000) => typeof value === "string" ? value.trim().slice(0, limit) : "";

const isDateKey = (value: string) => DATE_KEY.test(value) && !Number.isNaN(new Date(`${value}T12:00:00`).getTime());

export const blankWorkout = (): WorkoutLog => ({
  ladder: false,
  ladderRounds: 10,
  ladderMinutes: 60,
  ladderNotes: "",
  cindy: false,
  cindyRounds: 0,
  cindyMinutes: 20,
  cindyNotes: "",
});

export const blankEntry = (): JapaneseEntry => ({
  id: crypto.randomUUID(),
  type: "kotoba",
  content: "",
  reading: "",
  jlpt: "N3",
  studyMinutes: 15,
  sentence: "",
  sentenceMinutes: 5,
});

export const blankLog = (date: string): DailyLog => ({
  date,
  workout: blankWorkout(),
  japanese: [blankEntry()],
  freeMinutes: 0,
  note: "",
  updatedAt: new Date().toISOString(),
});

const defaultStore = (): TrackerStore => ({ version: 1, logs: {} });

export function readStore(): TrackerStore {
  try {
    const externalStorage = (window as Window & { storage?: { get?: (key: string) => string | null } }).storage;
    const raw = externalStorage?.get?.(STORAGE_KEY) ?? window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultStore();
    const parsed = JSON.parse(raw) as Partial<TrackerStore>;
    const logs = Object.entries(parsed.logs ?? {}).reduce<Record<string, DailyLog>>((next, [date, log]) => {
      if (!isDateKey(date) || !log) return next;
      next[date] = normalizeLog(date, log);
      return next;
    }, {});
    return { version: 1, logs, lastSyncedAt: typeof parsed.lastSyncedAt === "string" ? parsed.lastSyncedAt : undefined };
  } catch {
    return defaultStore();
  }
}

export function writeStore(store: TrackerStore): void {
  const payload = JSON.stringify(store);
  try {
    const externalStorage = (window as Window & { storage?: { set?: (key: string, value: string) => void } }).storage;
    externalStorage?.set?.(STORAGE_KEY, payload);
    window.localStorage.setItem(STORAGE_KEY, payload);
  } catch {
    // The UI continues to work in memory if a browser blocks storage.
  }
}

export function getLog(store: TrackerStore, date: string): DailyLog {
  return store.logs[date] ? structuredClone(store.logs[date]) : blankLog(date);
}

export function saveLog(store: TrackerStore, log: DailyLog): TrackerStore {
  const normalized = normalizeLog(log.date, log);
  return { ...store, logs: { ...store.logs, [normalized.date]: { ...normalized, updatedAt: new Date().toISOString() } } };
}

export const japaneseMinutes = (log: DailyLog) => log.japanese.reduce((sum, item) => item.content.trim() ? sum + safeMinutes(item.studyMinutes) + safeMinutes(item.sentenceMinutes) : sum, 0);
export const workoutMinutes = (log: DailyLog) => (log.workout.ladder ? safeMinutes(log.workout.ladderMinutes) : 0) + (log.workout.cindy ? safeMinutes(log.workout.cindyMinutes) : 0);
export const totalMinutes = (log: DailyLog) => japaneseMinutes(log) + workoutMinutes(log);
export const typeLabel: Record<JapaneseType, string> = { kotoba: "Kotoba", kanji: "Kanji", bunpou: "Bunpou" };

export const minutesForDate = (store: TrackerStore, date: string) => store.logs[date] ? totalMinutes(store.logs[date]) : 0;

export function normalizeLog(date: string, value: Partial<DailyLog>): DailyLog {
  const workout = value.workout ?? blankWorkout();
  const japanese: JapaneseEntry[] = Array.isArray(value.japanese) ? value.japanese.slice(0, 40).map((entry): JapaneseEntry => ({
    id: typeof entry?.id === "string" && entry.id ? entry.id.slice(0, 100) : crypto.randomUUID(),
    type: entry?.type === "kanji" || entry?.type === "bunpou" ? entry.type : "kotoba",
    content: safeText(entry?.content, 300),
    reading: safeText(entry?.reading, 300),
    jlpt: entry?.jlpt === "N5" || entry?.jlpt === "N4" ? entry.jlpt : "N3",
    studyMinutes: safeMinutes(entry?.studyMinutes),
    sentence: safeText(entry?.sentence, 600),
    sentenceMinutes: safeMinutes(entry?.sentenceMinutes),
  })) : [];
  return {
    date: isDateKey(date) ? date : isoDate(new Date()),
    workout: {
      ladder: Boolean(workout.ladder), ladderRounds: safeMinutes(workout.ladderRounds), ladderMinutes: safeMinutes(workout.ladderMinutes), ladderNotes: safeText(workout.ladderNotes, 600),
      cindy: Boolean(workout.cindy), cindyRounds: safeMinutes(workout.cindyRounds), cindyMinutes: safeMinutes(workout.cindyMinutes), cindyNotes: safeText(workout.cindyNotes, 600),
    },
    japanese: japanese.length ? japanese : [blankEntry()],
    freeMinutes: safeMinutes(value.freeMinutes),
    note: safeText(value.note, 600),
    updatedAt: typeof value.updatedAt === "string" ? value.updatedAt : new Date().toISOString(),
  };
}

export function isoDate(date: Date): string {
  return new Intl.DateTimeFormat("en-CA", { timeZone: "Asia/Jakarta" }).format(date);
}

export function formatDate(date: string, options: Intl.DateTimeFormatOptions = { weekday: "long", day: "numeric", month: "long" }): string {
  return new Intl.DateTimeFormat("id-ID", options).format(new Date(`${date}T12:00:00`));
}

export function rangeDates(from: string, to: string): string[] {
  if (!isDateKey(from) || !isDateKey(to) || from > to) return [];
  const dates: string[] = [];
  const cursor = new Date(`${from}T12:00:00`);
  const end = new Date(`${to}T12:00:00`);
  while (cursor <= end && dates.length < MAX_RANGE_DAYS) {
    dates.push(cursor.toISOString().slice(0, 10));
    cursor.setDate(cursor.getDate() + 1);
  }
  return dates;
}

export function getStats(store: TrackerStore, from: string, to: string) {
  const logs = rangeDates(from, to).map((date) => store.logs[date]).filter(Boolean) as DailyLog[];
  const byCategory = { kotoba: 0, kanji: 0, bunpou: 0, workout: 0 };
  logs.forEach((log) => {
    log.japanese.forEach((entry) => { if (entry.content.trim()) byCategory[entry.type] += safeMinutes(entry.studyMinutes) + safeMinutes(entry.sentenceMinutes); });
    byCategory.workout += workoutMinutes(log);
  });
  const activeDays = logs.filter((log) => totalMinutes(log) > 0).length;
  return { logs, byCategory, activeDays, totalMinutes: logs.reduce((sum, log) => sum + totalMinutes(log), 0), items: logs.reduce((sum, log) => sum + log.japanese.filter((x) => x.content.trim()).length, 0) };
}

export function getStreaks(store: TrackerStore, today = isoDate(new Date())) {
  const dates = Object.keys(store.logs).sort();
  if (!dates.length) return { current: 0, longest: 0 };
  let longest = 0;
  let run = 0;
  let previous = "";
  dates.forEach((date) => {
    if (totalMinutes(store.logs[date]) === 0) return;
    const gap = previous ? Math.round((new Date(`${date}T12:00:00`).getTime() - new Date(`${previous}T12:00:00`).getTime()) / 86400000) : 1;
    run = gap === 1 ? run + 1 : 1;
    longest = Math.max(longest, run);
    previous = date;
  });
  let current = 0;
  const cursor = new Date(`${today}T12:00:00`);
  while (true) {
    const key = cursor.toISOString().slice(0, 10);
    if (!store.logs[key] || totalMinutes(store.logs[key]) === 0) break;
    current += 1;
    cursor.setDate(cursor.getDate() - 1);
  }
  return { current, longest };
}
