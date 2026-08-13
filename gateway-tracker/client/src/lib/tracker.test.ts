/* Swiss Training Ledger: deterministic unit coverage for stats, range limits, and defensive data normalization. */

import { describe, expect, it } from "vitest";
import { DailyLog, TrackerStore, getStats, getStreaks, minutesForDate, normalizeLog, rangeDates, saveLog, totalMinutes } from "./tracker";

const createLog = (date: string, overrides: Partial<DailyLog> = {}): DailyLog => ({
  date,
  workout: { ladder: false, ladderRounds: 0, ladderMinutes: 0, ladderNotes: "", cindy: false, cindyRounds: 0, cindyMinutes: 0, cindyNotes: "" },
  japanese: [], freeMinutes: 0, note: "", updatedAt: "2026-08-13T00:00:00.000Z", ...overrides,
});

describe("tracker aggregation", () => {
  it("does not count empty Japanese rows and only includes selected workout minutes", () => {
    const log = createLog("2026-08-13", { workout: { ladder: true, ladderRounds: 10, ladderMinutes: 60, ladderNotes: "", cindy: false, cindyRounds: 0, cindyMinutes: 20, cindyNotes: "" }, japanese: [{ id: "empty", type: "kotoba", content: "", reading: "", jlpt: "N3", studyMinutes: 15, sentence: "", sentenceMinutes: 5 }] });
    expect(totalMinutes(log)).toBe(60);
  });

  it("keeps category totals consistent with the log total", () => {
    const store: TrackerStore = { version: 1, logs: { "2026-08-11": createLog("2026-08-11", { japanese: [{ id: "k", type: "kanji", content: "食", reading: "しょく", jlpt: "N3", studyMinutes: 20, sentence: "", sentenceMinutes: 5 }] }), "2026-08-12": createLog("2026-08-12", { workout: { ladder: false, ladderRounds: 0, ladderMinutes: 0, ladderNotes: "", cindy: true, cindyRounds: 14, cindyMinutes: 20, cindyNotes: "" } }) } };
    const stats = getStats(store, "2026-08-01", "2026-08-31");
    expect(stats.totalMinutes).toBe(45);
    expect(stats.byCategory).toEqual({ kotoba: 0, kanji: 25, bunpou: 0, workout: 20 });
  });

  it("calculates stable current and longest streaks", () => {
    const active = createLog("2026-08-13", { japanese: [{ id: "b", type: "bunpou", content: "〜はずだ", reading: "", jlpt: "N3", studyMinutes: 30, sentence: "", sentenceMinutes: 10 }] });
    const store: TrackerStore = { version: 1, logs: { "2026-08-10": active, "2026-08-11": { ...active, date: "2026-08-11" }, "2026-08-13": { ...active, date: "2026-08-13" } } };
    expect(getStreaks(store, "2026-08-13")).toEqual({ current: 1, longest: 2 });
  });

  it("rejects backwards ranges and bounds pathological ranges", () => {
    expect(rangeDates("2026-08-31", "2026-08-01")).toEqual([]);
    expect(rangeDates("2020-01-01", "2040-01-01")).toHaveLength(3660);
  });

  it("sanitizes malformed values before save and reads a date without cloning a blank log", () => {
    const cleaned = normalizeLog("2026-08-13", { freeMinutes: -7, japanese: [{ id: "a", type: "kotoba", content: "  覚える  ", reading: "", jlpt: "N3", studyMinutes: 9000, sentence: "", sentenceMinutes: Number.NaN }] });
    const saved = saveLog({ version: 1, logs: {} }, cleaned);
    expect(cleaned.freeMinutes).toBe(0);
    expect(cleaned.japanese[0].studyMinutes).toBe(1440);
    expect(minutesForDate(saved, "2026-08-12")).toBe(0);
  });
});
