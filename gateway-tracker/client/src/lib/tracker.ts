/* Local-first journal: defensive storage, batch study aggregation, and deterministic daily planning. */

export type JapaneseType = "kotoba" | "kanji" | "bunpou";
export type WeeklyCategory = JapaneseType | "workout";
export type JLPTLevel = "N5" | "N4" | "N3";
export type JapaneseChecklist = Record<JapaneseType, boolean>;

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

export interface JapaneseBatch {
  id: string;
  type: JapaneseType;
  jlpt: JLPTLevel;
  items: string[];
  studyMinutes: number;
  sentenceMinutes: number;
  note: string;
  createdAt: string;
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

export type SessionKind = JapaneseType | "ladder" | "cindy";
export type SessionSelection = Record<SessionKind, boolean>;
export type LadderExercise = "pullups" | "dips" | "pressups" | "situps" | "airSquats";
export type CindyExercise = "pullups" | "pressups" | "airSquats";
export const cindyTargetPresets = [10, 20, 27] as const;
export type CindyTarget = (typeof cindyTargetPresets)[number];
export interface SessionDraft {
  date: string;
  selected: SessionSelection;
  ladderChecks: Record<LadderExercise, boolean[]>;
  cindyChecks: Record<CindyExercise, boolean[]>;
  ladderRounds: boolean[];
  cindyRounds: boolean[];
  cindyTarget: CindyTarget;
  cindyTimerDone: boolean;
  japaneseBlocks: Record<JapaneseType, boolean[]>;
}

export interface DailyLog {
  date: string;
  workout: WorkoutLog;
  activities?: JapaneseChecklist;
  milestoneMinutes?: Record<JapaneseType, number>;
  milestoneItems?: Record<JapaneseType, number>;
  japanese: JapaneseEntry[];
  batches?: JapaneseBatch[];
  freeMinutes: number;
  note: string;
  updatedAt: string;
}

export interface TrackerSettings {
  dailyJapaneseTarget: number;
  focusBlockMinutes: number;
  dailyReminderTime: string;
  weeklyTargets: Record<WeeklyCategory, number>;
}

export interface TrackerStore {
  version: 1;
  logs: Record<string, DailyLog>;
  lastSyncedAt?: string;
  settings?: TrackerSettings;
  drafts?: Record<string, SessionDraft>;
}

export interface DailyPlan {
  targetMinutes: number;
  completedMinutes: number;
  remainingMinutes: number;
  recommendedBlockMinutes: number;
  missedDays: number;
  sevenDayAverage: number;
  priority: JapaneseType;
  instruction: string;
}

export interface WeeklyProgress {
  category: WeeklyCategory;
  target: number;
  completed: number;
  remaining: number;
  percentage: number;
}

const STORAGE_KEY = "gateway-tracker-v1";
const MAX_RANGE_DAYS = 3660;
const MAX_BATCHES_PER_DAY = 100;
const MAX_ITEMS_PER_BATCH = 1000;
const DATE_KEY = /^\d{4}-\d{2}-\d{2}$/;
export const ladderRoundNumbers = [...Array.from({ length: 10 }, (_, index) => index + 1), ...Array.from({ length: 9 }, (_, index) => 9 - index)];
export const cindyRepsPerRound = 30;
export const japaneseMilestonePlan: Record<JapaneseType, { blocks: number; itemsPerBlock: number; minutesPerBlock: number }> = { kotoba: { blocks: 5, itemsPerBlock: 100, minutesPerBlock: 20 }, kanji: { blocks: 3, itemsPerBlock: 10, minutesPerBlock: 15 }, bunpou: { blocks: 3, itemsPerBlock: 1, minutesPerBlock: 15 } };
export const ladderExercisePlan: Array<{ key: LadderExercise; label: string; multiplier: number }> = [{ key: "pullups", label: "Pull-up", multiplier: 1 }, { key: "dips", label: "Dip", multiplier: 2 }, { key: "pressups", label: "Press-up", multiplier: 3 }, { key: "situps", label: "Sit-up", multiplier: 4 }, { key: "airSquats", label: "Air squat", multiplier: 5 }];
export const cindyExercisePlan: Array<{ key: CindyExercise; label: string; reps: number }> = [{ key: "pullups", label: "Pull-up", reps: 5 }, { key: "pressups", label: "Press-up", reps: 10 }, { key: "airSquats", label: "Air squat", reps: 15 }];

const safeMinutes = (value: unknown) => {
  const numeric = Number(value);
  return Number.isFinite(numeric) ? Math.max(0, Math.min(1440, Math.round(numeric))) : 0;
};

const safeText = (value: unknown, limit = 1000) => typeof value === "string" ? value.trim().slice(0, limit) : "";
const isDateKey = (value: string) => DATE_KEY.test(value) && !Number.isNaN(new Date(`${value}T12:00:00`).getTime());

export const blankWorkout = (): WorkoutLog => ({ ladder: false, ladderRounds: 10, ladderMinutes: 60, ladderNotes: "", cindy: false, cindyRounds: 0, cindyMinutes: 20, cindyNotes: "" });
export const japaneseChecklistMinutes: Record<JapaneseType, number> = { kotoba: 25, kanji: 20, bunpou: 20 };
export const blankJapaneseChecklist = (): JapaneseChecklist => ({ kotoba: false, kanji: false, bunpou: false });
export const blankEntry = (): JapaneseEntry => ({ id: crypto.randomUUID(), type: "kotoba", content: "", reading: "", jlpt: "N3", studyMinutes: 15, sentence: "", sentenceMinutes: 5 });
export const blankLog = (date: string): DailyLog => ({ date, workout: blankWorkout(), activities: blankJapaneseChecklist(), japanese: [blankEntry()], batches: [], freeMinutes: 0, note: "", updatedAt: new Date().toISOString() });
export const blankSessionDraft = (date: string): SessionDraft => ({ date, selected: { kotoba: false, kanji: false, bunpou: false, ladder: false, cindy: false }, ladderChecks: { pullups: ladderRoundNumbers.map(() => false), dips: ladderRoundNumbers.map(() => false), pressups: ladderRoundNumbers.map(() => false), situps: ladderRoundNumbers.map(() => false), airSquats: ladderRoundNumbers.map(() => false) }, cindyChecks: { pullups: Array.from({ length: 20 }, () => false), pressups: Array.from({ length: 20 }, () => false), airSquats: Array.from({ length: 20 }, () => false) }, ladderRounds: ladderRoundNumbers.map(() => false), cindyRounds: Array.from({ length: 30 }, () => false), cindyTarget: 20, cindyTimerDone: false, japaneseBlocks: { kotoba: Array.from({ length: japaneseMilestonePlan.kotoba.blocks }, () => false), kanji: Array.from({ length: japaneseMilestonePlan.kanji.blocks }, () => false), bunpou: Array.from({ length: japaneseMilestonePlan.bunpou.blocks }, () => false) } });

const defaultWeeklyTargets = (): Record<WeeklyCategory, number> => ({ kotoba: 120, kanji: 75, bunpou: 60, workout: 120 });
const safeWeeklyTarget = (value: unknown, fallback: number) => Number.isFinite(Number(value)) ? Math.max(0, Math.min(2400, Math.round(Number(value)))) : fallback;
export const defaultSettings = (): TrackerSettings => ({ dailyJapaneseTarget: 45, focusBlockMinutes: 25, dailyReminderTime: "19:30", weeklyTargets: defaultWeeklyTargets() });
const normalizeSettings = (value?: Partial<TrackerSettings>): TrackerSettings => ({
  dailyJapaneseTarget: Math.max(15, Math.min(180, safeMinutes(value?.dailyJapaneseTarget) || 45)),
  focusBlockMinutes: Math.max(5, Math.min(90, safeMinutes(value?.focusBlockMinutes) || 25)),
  dailyReminderTime: /^([01]\d|2[0-3]):[0-5]\d$/.test(value?.dailyReminderTime ?? "") ? value?.dailyReminderTime as string : "19:30",
  weeklyTargets: (Object.keys(defaultWeeklyTargets()) as WeeklyCategory[]).reduce<Record<WeeklyCategory, number>>((targets, category) => {
    targets[category] = safeWeeklyTarget(value?.weeklyTargets?.[category], defaultWeeklyTargets()[category]);
    return targets;
  }, defaultWeeklyTargets()),
});
const defaultStore = (): TrackerStore => ({ version: 1, logs: {}, drafts: {}, settings: defaultSettings() });
export const getSettings = (store: TrackerStore) => normalizeSettings(store.settings);
export const saveSettings = (store: TrackerStore, settings: Partial<TrackerSettings>): TrackerStore => ({ ...store, settings: normalizeSettings({ ...getSettings(store), ...settings }) });

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
    const drafts = Object.entries(parsed.drafts ?? {}).reduce<Record<string, SessionDraft>>((next, [date, draft]) => {
      if (!isDateKey(date) || !draft) return next;
      next[date] = normalizeDraft(date, draft);
      return next;
    }, {});
    return { version: 1, logs, drafts, lastSyncedAt: typeof parsed.lastSyncedAt === "string" ? parsed.lastSyncedAt : undefined, settings: normalizeSettings(parsed.settings) };
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
    // In-memory UI remains usable if browser storage is blocked.
  }
}

export function getLog(store: TrackerStore, date: string): DailyLog {
  return store.logs[date] ? structuredClone(store.logs[date]) : blankLog(date);
}

export function saveLog(store: TrackerStore, log: DailyLog): TrackerStore {
  const normalized = normalizeLog(log.date, log);
  return { ...store, logs: { ...store.logs, [normalized.date]: { ...normalized, updatedAt: new Date().toISOString() } } };
}

export function normalizeDraft(date: string, value?: Partial<SessionDraft>): SessionDraft {
  const fallback = blankSessionDraft(date);
  const selected = (Object.keys(fallback.selected) as SessionKind[]).reduce<SessionSelection>((next, key) => ({ ...next, [key]: Boolean(value?.selected?.[key]) }), fallback.selected);
  const flagList = (source: unknown, length: number) => Array.from({ length }, (_, index) => Boolean(Array.isArray(source) && source[index]));
  const rawCindyTarget = Number(value?.cindyTarget);
  const cindyTarget: CindyTarget = cindyTargetPresets.includes(rawCindyTarget as CindyTarget) ? rawCindyTarget as CindyTarget : 20;
  return { date: isDateKey(date) ? date : isoDate(new Date()), selected, ladderChecks: { pullups: flagList(value?.ladderChecks?.pullups, ladderRoundNumbers.length), dips: flagList(value?.ladderChecks?.dips, ladderRoundNumbers.length), pressups: flagList(value?.ladderChecks?.pressups, ladderRoundNumbers.length), situps: flagList(value?.ladderChecks?.situps, ladderRoundNumbers.length), airSquats: flagList(value?.ladderChecks?.airSquats, ladderRoundNumbers.length) }, cindyChecks: { pullups: flagList(value?.cindyChecks?.pullups, cindyTarget), pressups: flagList(value?.cindyChecks?.pressups, cindyTarget), airSquats: flagList(value?.cindyChecks?.airSquats, cindyTarget) }, ladderRounds: flagList(value?.ladderRounds, ladderRoundNumbers.length), cindyRounds: flagList(value?.cindyRounds, 30), cindyTarget, cindyTimerDone: Boolean(value?.cindyTimerDone), japaneseBlocks: { kotoba: flagList(value?.japaneseBlocks?.kotoba, japaneseMilestonePlan.kotoba.blocks), kanji: flagList(value?.japaneseBlocks?.kanji, japaneseMilestonePlan.kanji.blocks), bunpou: flagList(value?.japaneseBlocks?.bunpou, japaneseMilestonePlan.bunpou.blocks) } };
}

export function getDraft(store: TrackerStore, date: string): SessionDraft { return normalizeDraft(date, store.drafts?.[date]); }
export function saveDraft(store: TrackerStore, draft: SessionDraft): TrackerStore { const normalized = normalizeDraft(draft.date, draft); return { ...store, drafts: { ...store.drafts, [normalized.date]: normalized } }; }
export function checkedCount(values: boolean[]) { return values.filter(Boolean).length; }
export function ladderRoundComplete(draft: SessionDraft, index: number) { return ladderExercisePlan.every((exercise) => draft.ladderChecks[exercise.key][index]); }
export function cindyRoundComplete(draft: SessionDraft, index: number) { return cindyExercisePlan.every((exercise) => draft.cindyChecks[exercise.key][index]); }
export function ladderRoundsComplete(draft: SessionDraft) { return ladderRoundNumbers.filter((_, index) => ladderRoundComplete(draft, index)).length; }
export function cindyRoundsComplete(draft: SessionDraft) { return Array.from({ length: draft.cindyTarget }, (_, index) => cindyRoundComplete(draft, index)).filter(Boolean).length; }
export function ladderReps(draft: SessionDraft) { return ladderExercisePlan.reduce((sum, exercise) => sum + draft.ladderChecks[exercise.key].reduce((exerciseTotal, checked, index) => exerciseTotal + (checked ? ladderRoundNumbers[index] * exercise.multiplier : 0), 0), 0); }
export function cindyReps(draft: SessionDraft) { return cindyExercisePlan.reduce((sum, exercise) => sum + checkedCount(draft.cindyChecks[exercise.key].slice(0, draft.cindyTarget)) * exercise.reps, 0); }
export function cindyProgress(draft: SessionDraft) { const milestones = cindyExercisePlan.reduce((sum, exercise) => sum + checkedCount(draft.cindyChecks[exercise.key].slice(0, draft.cindyTarget)), 0); const totalMilestones = cindyExercisePlan.length * draft.cindyTarget; const percentage = Math.round((milestones / totalMilestones) * 100); const estimatedMinutes = draft.cindyTimerDone ? 20 : Math.min(20, Math.max(0, Math.round((percentage / 100) * 20))); return { targetRounds: draft.cindyTarget, milestones, totalMilestones, percentage, estimatedMinutes, completedRounds: cindyRoundsComplete(draft), reps: cindyReps(draft) }; }
export function japaneseDraftMinutes(draft: SessionDraft, type: JapaneseType) { const plan = japaneseMilestonePlan[type]; return checkedCount(draft.japaneseBlocks[type]) * plan.minutesPerBlock; }
export function japaneseDraftItems(draft: SessionDraft, type: JapaneseType) { const plan = japaneseMilestonePlan[type]; return checkedCount(draft.japaneseBlocks[type]) * plan.itemsPerBlock; }
export function isDraftComplete(draft: SessionDraft) {
  const selectedKinds = (Object.keys(draft.selected) as SessionKind[]).filter((kind) => draft.selected[kind]);
  if (!selectedKinds.length) return false;
  return selectedKinds.every((kind) => kind === "ladder" ? ladderRoundNumbers.every((_, index) => ladderRoundComplete(draft, index)) : kind === "cindy" ? draft.cindyTimerDone && cindyRoundsComplete(draft) === draft.cindyTarget : draft.japaneseBlocks[kind].every(Boolean));
}

export function submitDraft(store: TrackerStore, date: string): TrackerStore {
  const draft = getDraft(store, date);
  if (!isDraftComplete(draft)) return store;
  const existing = getLog(store, date);
  const milestoneMinutes = (Object.keys(japaneseMilestonePlan) as JapaneseType[]).reduce<Record<JapaneseType, number>>((next, type) => ({ ...next, [type]: draft.selected[type] ? japaneseDraftMinutes(draft, type) : 0 }), { kotoba: 0, kanji: 0, bunpou: 0 });
  const milestoneItems = (Object.keys(japaneseMilestonePlan) as JapaneseType[]).reduce<Record<JapaneseType, number>>((next, type) => ({ ...next, [type]: draft.selected[type] ? japaneseDraftItems(draft, type) : 0 }), { kotoba: 0, kanji: 0, bunpou: 0 });
  const log = normalizeLog(date, { ...existing, activities: blankJapaneseChecklist(), japanese: [], batches: [], milestoneMinutes, milestoneItems, workout: { ...blankWorkout(), ladder: draft.selected.ladder, ladderRounds: draft.selected.ladder ? ladderRoundsComplete(draft) : 0, ladderMinutes: draft.selected.ladder ? 60 : 0, cindy: draft.selected.cindy, cindyRounds: draft.selected.cindy ? cindyRoundsComplete(draft) : 0, cindyMinutes: draft.selected.cindy ? 20 : 0 } });
  const { [date]: _submitted, ...drafts } = store.drafts ?? {};
  return { ...saveLog(store, log), drafts };
}

export const batchItemCount = (batch: JapaneseBatch) => batch.items.length;
export const batchMinutes = (batch: JapaneseBatch) => batch.items.length ? safeMinutes(batch.studyMinutes) + safeMinutes(batch.sentenceMinutes) : 0;
export const japaneseBatches = (log: DailyLog) => log.batches ?? [];
export const japaneseChecklist = (log: DailyLog): JapaneseChecklist => ({ ...blankJapaneseChecklist(), ...log.activities });
export const japaneseChecklistTotal = (log: DailyLog) => (Object.keys(japaneseChecklistMinutes) as JapaneseType[]).reduce((sum, type) => sum + (japaneseChecklist(log)[type] ? japaneseChecklistMinutes[type] : 0), 0);
export const completedJapaneseChecks = (log: DailyLog) => (Object.keys(japaneseChecklistMinutes) as JapaneseType[]).filter((type) => japaneseChecklist(log)[type]).length;
export const milestoneMinutes = (log: DailyLog, type: JapaneseType) => safeMinutes(log.milestoneMinutes?.[type]);
export const milestoneItems = (log: DailyLog, type: JapaneseType) => safeMinutes(log.milestoneItems?.[type]);
export const japaneseItemCount = (log: DailyLog) => (Object.keys(japaneseMilestonePlan) as JapaneseType[]).reduce((sum, type) => sum + milestoneItems(log, type), 0) + log.japanese.filter((item) => item.content.trim()).length + japaneseBatches(log).reduce((sum, batch) => sum + batchItemCount(batch), 0);
export const categoryJapaneseMinutes = (log: DailyLog, type: JapaneseType) => milestoneMinutes(log, type) + (japaneseChecklist(log)[type] ? japaneseChecklistMinutes[type] : 0) + log.japanese.filter((item) => item.content.trim() && item.type === type).reduce((sum, item) => sum + safeMinutes(item.studyMinutes) + safeMinutes(item.sentenceMinutes), 0) + japaneseBatches(log).filter((batch) => batch.type === type).reduce((sum, batch) => sum + batchMinutes(batch), 0);
export const japaneseMinutes = (log: DailyLog) => (Object.keys(japaneseMilestonePlan) as JapaneseType[]).reduce((sum, type) => sum + milestoneMinutes(log, type), 0) + japaneseChecklistTotal(log) + log.japanese.reduce((sum, item) => item.content.trim() ? sum + safeMinutes(item.studyMinutes) + safeMinutes(item.sentenceMinutes) : sum, 0) + japaneseBatches(log).reduce((sum, batch) => sum + batchMinutes(batch), 0);
export const workoutMinutes = (log: DailyLog) => (log.workout.ladder ? safeMinutes(log.workout.ladderMinutes) : 0) + (log.workout.cindy ? safeMinutes(log.workout.cindyMinutes) : 0);
export const totalMinutes = (log: DailyLog) => japaneseMinutes(log) + workoutMinutes(log);
export const typeLabel: Record<JapaneseType, string> = { kotoba: "Kotoba", kanji: "Kanji", bunpou: "Bunpou" };
export const minutesForDate = (store: TrackerStore, date: string) => store.logs[date] ? totalMinutes(store.logs[date]) : 0;

export function normalizeLog(date: string, value: Partial<DailyLog>): DailyLog {
  const workout = value.workout ?? blankWorkout();
  const japanese: JapaneseEntry[] = Array.isArray(value.japanese) ? value.japanese.slice(0, 40).map((entry): JapaneseEntry => ({
    id: typeof entry?.id === "string" && entry.id ? entry.id.slice(0, 100) : crypto.randomUUID(),
    type: entry?.type === "kanji" || entry?.type === "bunpou" ? entry.type : "kotoba",
    content: safeText(entry?.content, 300), reading: safeText(entry?.reading, 300), jlpt: entry?.jlpt === "N5" || entry?.jlpt === "N4" ? entry.jlpt : "N3",
    studyMinutes: safeMinutes(entry?.studyMinutes), sentence: safeText(entry?.sentence, 600), sentenceMinutes: safeMinutes(entry?.sentenceMinutes),
  })) : [];
  const batches: JapaneseBatch[] = Array.isArray(value.batches) ? value.batches.slice(0, MAX_BATCHES_PER_DAY).map((batch): JapaneseBatch => ({
    id: typeof batch?.id === "string" && batch.id ? batch.id.slice(0, 100) : crypto.randomUUID(),
    type: batch?.type === "kanji" || batch?.type === "bunpou" ? batch.type : "kotoba",
    jlpt: batch?.jlpt === "N5" || batch?.jlpt === "N4" ? batch.jlpt : "N3",
    items: Array.isArray(batch?.items) ? Array.from(new Set(batch.items.map((item) => safeText(item, 160)).filter(Boolean))).slice(0, MAX_ITEMS_PER_BATCH) : [],
    studyMinutes: safeMinutes(batch?.studyMinutes), sentenceMinutes: safeMinutes(batch?.sentenceMinutes), note: safeText(batch?.note, 300), createdAt: typeof batch?.createdAt === "string" ? batch.createdAt : new Date().toISOString(),
  })).filter((batch) => batch.items.length > 0) : [];
  return {
    date: isDateKey(date) ? date : isoDate(new Date()),
    workout: { ladder: Boolean(workout.ladder), ladderRounds: safeMinutes(workout.ladderRounds), ladderMinutes: safeMinutes(workout.ladderMinutes), ladderNotes: safeText(workout.ladderNotes, 600), cindy: Boolean(workout.cindy), cindyRounds: safeMinutes(workout.cindyRounds), cindyMinutes: safeMinutes(workout.cindyMinutes), cindyNotes: safeText(workout.cindyNotes, 600) },
    activities: { kotoba: Boolean(value.activities?.kotoba), kanji: Boolean(value.activities?.kanji), bunpou: Boolean(value.activities?.bunpou) },
    milestoneMinutes: { kotoba: safeMinutes(value.milestoneMinutes?.kotoba), kanji: safeMinutes(value.milestoneMinutes?.kanji), bunpou: safeMinutes(value.milestoneMinutes?.bunpou) },
    milestoneItems: { kotoba: safeMinutes(value.milestoneItems?.kotoba), kanji: safeMinutes(value.milestoneItems?.kanji), bunpou: safeMinutes(value.milestoneItems?.bunpou) },
    japanese: japanese.length ? japanese : [blankEntry()], batches, freeMinutes: safeMinutes(value.freeMinutes), note: safeText(value.note, 600), updatedAt: typeof value.updatedAt === "string" ? value.updatedAt : new Date().toISOString(),
  };
}

export function isoDate(date: Date): string { return new Intl.DateTimeFormat("en-CA", { timeZone: "Asia/Jakarta" }).format(date); }
export function formatDate(date: string, options: Intl.DateTimeFormatOptions = { weekday: "long", day: "numeric", month: "long" }): string { return new Intl.DateTimeFormat("id-ID", options).format(new Date(`${date}T12:00:00`)); }

export function rangeDates(from: string, to: string): string[] {
  if (!isDateKey(from) || !isDateKey(to) || from > to) return [];
  const dates: string[] = [];
  const cursor = new Date(`${from}T12:00:00`);
  const end = new Date(`${to}T12:00:00`);
  while (cursor <= end && dates.length < MAX_RANGE_DAYS) { dates.push(cursor.toISOString().slice(0, 10)); cursor.setDate(cursor.getDate() + 1); }
  return dates;
}

export function getStats(store: TrackerStore, from: string, to: string) {
  const logs = rangeDates(from, to).map((date) => store.logs[date]).filter(Boolean) as DailyLog[];
  const byCategory = { kotoba: 0, kanji: 0, bunpou: 0, workout: 0 };
  logs.forEach((log) => {
    (Object.keys(japaneseChecklistMinutes) as JapaneseType[]).forEach((type) => { byCategory[type] += categoryJapaneseMinutes(log, type); });
    byCategory.workout += workoutMinutes(log);
  });
  const activeDays = logs.filter((log) => totalMinutes(log) > 0).length;
  return { logs, byCategory, activeDays, totalMinutes: logs.reduce((sum, log) => sum + totalMinutes(log), 0), items: logs.reduce((sum, log) => sum + japaneseItemCount(log), 0) };
}

export function weekRange(date = isoDate(new Date())) {
  const cursor = new Date(`${date}T12:00:00`);
  const offset = (cursor.getDay() + 6) % 7;
  cursor.setDate(cursor.getDate() - offset);
  const from = cursor.toISOString().slice(0, 10);
  cursor.setDate(cursor.getDate() + 6);
  return { from, to: cursor.toISOString().slice(0, 10) };
}

export function getWeeklyProgress(store: TrackerStore, date = isoDate(new Date())): { from: string; to: string; progress: WeeklyProgress[] } {
  const { from, to } = weekRange(date);
  const stats = getStats(store, from, to).byCategory;
  const targets = getSettings(store).weeklyTargets;
  const progress = (Object.keys(targets) as WeeklyCategory[]).map((category) => {
    const target = targets[category];
    const completed = stats[category];
    return { category, target, completed, remaining: Math.max(0, target - completed), percentage: target ? Math.min(100, Math.round((completed / target) * 100)) : 0 };
  });
  return { from, to, progress };
}

function previousDate(date: string, offset: number): string {
  const cursor = new Date(`${date}T12:00:00`);
  cursor.setDate(cursor.getDate() - offset);
  return cursor.toISOString().slice(0, 10);
}

export function getDailyPlan(store: TrackerStore, today = isoDate(new Date())): DailyPlan {
  const settings = getSettings(store);
  const current = store.logs[today] ? japaneseMinutes(store.logs[today]) : 0;
  const history = Array.from({ length: 7 }, (_, index) => { const log = store.logs[previousDate(today, index + 1)]; return log ? japaneseMinutes(log) : 0; });
  const sevenDayAverage = Math.round(history.reduce((sum, value) => sum + value, 0) / history.length);
  let missedDays = 0;
  for (let index = 1; index <= 7; index += 1) { const log = store.logs[previousDate(today, index)]; if (!log || japaneseMinutes(log) === 0) missedDays += 1; else break; }
  const reentryDiscount = missedDays >= 3 ? Math.min(20, missedDays * 4) : missedDays ? 5 : 0;
  const consistencyAdjust = sevenDayAverage >= settings.dailyJapaneseTarget * 0.9 ? 5 : 0;
  const targetMinutes = Math.max(25, Math.min(90, settings.dailyJapaneseTarget - reentryDiscount + consistencyAdjust));
  const recent = getStats(store, previousDate(today, 14), today).byCategory;
  const weights: Record<JapaneseType, number> = { kotoba: 0.5, kanji: 0.3, bunpou: 0.2 };
  const japaneseTotal = Math.max(1, recent.kotoba + recent.kanji + recent.bunpou);
  const priority = (Object.keys(weights) as JapaneseType[]).sort((a, b) => (weights[b] - recent[b] / japaneseTotal) - (weights[a] - recent[a] / japaneseTotal))[0];
  const remainingMinutes = Math.max(0, targetMinutes - current);
  const recommendedBlockMinutes = remainingMinutes ? Math.min(settings.focusBlockMinutes, remainingMinutes) : 0;
  const instruction = remainingMinutes === 0 ? "Target Jepang hari ini sudah selesai. Simpan, istirahat, atau tambah review ringan." : `Mulai ${recommendedBlockMinutes} menit ${typeLabel[priority].toLowerCase()}; sisa ${remainingMinutes} menit untuk menutup target hari ini.`;
  return { targetMinutes, completedMinutes: current, remainingMinutes, recommendedBlockMinutes, missedDays, sevenDayAverage, priority, instruction };
}

export function getStreaks(store: TrackerStore, today = isoDate(new Date())) {
  const dates = Object.keys(store.logs).sort();
  if (!dates.length) return { current: 0, longest: 0 };
  let longest = 0; let run = 0; let previous = "";
  dates.forEach((date) => { if (totalMinutes(store.logs[date]) === 0) return; const gap = previous ? Math.round((new Date(`${date}T12:00:00`).getTime() - new Date(`${previous}T12:00:00`).getTime()) / 86400000) : 1; run = gap === 1 ? run + 1 : 1; longest = Math.max(longest, run); previous = date; });
  let current = 0; const cursor = new Date(`${today}T12:00:00`);
  while (true) { const key = cursor.toISOString().slice(0, 10); if (!store.logs[key] || totalMinutes(store.logs[key]) === 0) break; current += 1; cursor.setDate(cursor.getDate() - 1); }
  return { current, longest };
}
