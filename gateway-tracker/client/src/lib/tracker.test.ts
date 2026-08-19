/* Swiss Training Ledger: deterministic unit coverage for stats, range limits, and defensive data normalization. */

import { describe, expect, it } from "vitest";
import { blankSessionDraft, cindyExercisePlan, cindyProgress, cindyReps, DailyLog, getDailyPlan, getStats, getStreaks, getWeeklyProgress, isDraftComplete, japaneseItemCount, ladderExercisePlan, ladderReps, minutesForDate, normalizeLog, rangeDates, saveDraft, saveLog, submitDraft, totalMinutes, TrackerStore, weekRange } from "./tracker";

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

  it("aggregates a 500-item batch without expanding it into manual entry work", () => {
    const items = Array.from({ length: 500 }, (_, index) => `語彙${index}`);
    const log = normalizeLog("2026-08-13", { japanese: [], batches: [{ id: "batch", type: "kotoba", jlpt: "N3", items, studyMinutes: 180, sentenceMinutes: 20, note: "SRS import", createdAt: "2026-08-13T00:00:00.000Z" }] });
    expect(japaneseItemCount(log)).toBe(500);
    expect(totalMinutes(log)).toBe(200);
  });

  it("uses a bounded re-entry target after missed sessions and recommends an underrepresented category", () => {
    const store: TrackerStore = { version: 1, logs: { "2026-08-10": createLog("2026-08-10", { japanese: [{ id: "k", type: "kanji", content: "食", reading: "しょく", jlpt: "N3", studyMinutes: 45, sentence: "", sentenceMinutes: 0 }] }) } };
    const plan = getDailyPlan(store, "2026-08-13");
    expect(plan.targetMinutes).toBeLessThan(45);
    expect(plan.recommendedBlockMinutes).toBeGreaterThan(0);
    expect(plan.priority).toBe("kotoba");
  });

  it("aggregates Monday–Sunday targets across manual, batch, and workout progress", () => {
    const monday = createLog("2026-08-10", { japanese: [{ id: "k", type: "kotoba", content: "覚える", reading: "", jlpt: "N3", studyMinutes: 20, sentence: "", sentenceMinutes: 0 }], batches: [{ id: "batch", type: "kanji", jlpt: "N3", items: ["食", "飲"], studyMinutes: 30, sentenceMinutes: 0, note: "", createdAt: "2026-08-10T00:00:00.000Z" }] });
    const sunday = createLog("2026-08-16", { workout: { ladder: true, ladderRounds: 10, ladderMinutes: 45, ladderNotes: "", cindy: false, cindyRounds: 0, cindyMinutes: 0, cindyNotes: "" }, japanese: [{ id: "b", type: "bunpou", content: "〜わけではない", reading: "", jlpt: "N3", studyMinutes: 25, sentence: "", sentenceMinutes: 5 }] });
    const nextWeek = createLog("2026-08-17", { japanese: [{ id: "next", type: "kotoba", content: "翌週", reading: "", jlpt: "N3", studyMinutes: 99, sentence: "", sentenceMinutes: 0 }] });
    const store: TrackerStore = { version: 1, logs: { "2026-08-10": monday, "2026-08-16": sunday, "2026-08-17": nextWeek }, settings: { dailyJapaneseTarget: 45, focusBlockMinutes: 25, dailyReminderTime: "19:30", weeklyTargets: { kotoba: 40, kanji: 30, bunpou: 30, workout: 60 } } };
    const weekly = getWeeklyProgress(store, "2026-08-14");
    expect(weekRange("2026-08-16")).toEqual({ from: "2026-08-10", to: "2026-08-16" });
    expect(weekly.progress).toEqual([
      { category: "kotoba", target: 40, completed: 20, remaining: 20, percentage: 50 },
      { category: "kanji", target: 30, completed: 30, remaining: 0, percentage: 100 },
      { category: "bunpou", target: 30, completed: 30, remaining: 0, percentage: 100 },
      { category: "workout", target: 60, completed: 45, remaining: 15, percentage: 75 },
    ]);
  });

  it("counts a checked daily activity and completed workout with their prescribed minutes", () => {
    const log = normalizeLog("2026-08-14", { activities: { kotoba: true, kanji: false, bunpou: true }, workout: { ladder: false, ladderRounds: 0, ladderMinutes: 60, ladderNotes: "", cindy: true, cindyRounds: 0, cindyMinutes: 20, cindyNotes: "" } });
    const store: TrackerStore = { version: 1, logs: { "2026-08-14": log } };
    expect(totalMinutes(log)).toBe(65);
    expect(getStats(store, "2026-08-14", "2026-08-14").byCategory).toEqual({ kotoba: 25, kanji: 0, bunpou: 20, workout: 20 });
  });

  it("keeps partial milestone checks out of history until a selected session is complete", () => {
    const draft = blankSessionDraft("2026-08-18");
    draft.selected.ladder = true;
    draft.ladderChecks.pullups[0] = true;
    const pending = saveDraft({ version: 1, logs: {} }, draft);
    expect(isDraftComplete(draft)).toBe(false);
    expect(submitDraft(pending, "2026-08-18").logs).toEqual({});
    expect(pending.drafts?.["2026-08-18"]?.ladderChecks.pullups[0]).toBe(true);
    expect(getWeeklyProgress(pending, "2026-08-18").progress.find((item) => item.category === "workout")?.completed).toBe(0);
  });

  it("calculates workout and Japanese milestones only at atomic session submit", () => {
    const draft = blankSessionDraft("2026-08-18");
    draft.selected.ladder = true;
    draft.selected.cindy = true;
    draft.selected.kotoba = true;
    draft.cindyTarget = 27;
    ladderExercisePlan.forEach((exercise) => { draft.ladderChecks[exercise.key] = draft.ladderChecks[exercise.key].map(() => true); });
    cindyExercisePlan.forEach((exercise) => { draft.cindyChecks[exercise.key] = Array.from({ length: 27 }, () => true); });
    draft.cindyTimerDone = true;
    draft.japaneseBlocks.kotoba = draft.japaneseBlocks.kotoba.map(() => true);
    expect(ladderReps(draft)).toBe(1500);
    expect(cindyReps(draft)).toBe(810);
    expect(cindyProgress(draft)).toMatchObject({ targetRounds: 27, completedRounds: 27, reps: 810, percentage: 100, estimatedMinutes: 20 });
    expect(isDraftComplete(draft)).toBe(true);
    const submitted = submitDraft(saveDraft({ version: 1, logs: {} }, draft), "2026-08-18");
    const log = submitted.logs["2026-08-18"];
    expect(log.workout).toMatchObject({ ladder: true, ladderRounds: 19, ladderMinutes: 60, cindy: true, cindyRounds: 27, cindyMinutes: 20 });
    expect(japaneseItemCount(log)).toBe(500);
    expect(totalMinutes(log)).toBe(180);
    expect(submitted.drafts?.["2026-08-18"]).toBeUndefined();
    expect(getWeeklyProgress(submitted, "2026-08-18").progress).toEqual(expect.arrayContaining([
      expect.objectContaining({ category: "kotoba", completed: 100 }),
      expect.objectContaining({ category: "workout", completed: 80 }),
    ]));
    expect(submitDraft(submitted, "2026-08-18")).toBe(submitted);
  });

  it("estimates Cindy pace from partial 5–10–15 milestones before the timer closes", () => {
    const draft = blankSessionDraft("2026-08-18");
    draft.selected.cindy = true;
    cindyExercisePlan.forEach((exercise) => { draft.cindyChecks[exercise.key] = draft.cindyChecks[exercise.key].map((_, index) => index < 3); });
    expect(cindyProgress(draft)).toEqual({ targetRounds: 20, milestones: 9, totalMilestones: 60, percentage: 15, estimatedMinutes: 3, completedRounds: 3, reps: 90 });
  });

  it("uses each Cindy preset as the completion and pace denominator", () => {
    ([10, 20, 27] as const).forEach((target) => {
      const draft = blankSessionDraft("2026-08-18");
      draft.selected.cindy = true;
      draft.cindyTarget = target;
      cindyExercisePlan.forEach((exercise) => { draft.cindyChecks[exercise.key] = Array.from({ length: target }, () => true); });
      draft.cindyTimerDone = true;
      expect(cindyProgress(draft)).toMatchObject({ targetRounds: target, totalMilestones: target * 3, percentage: 100, completedRounds: target, reps: target * 30, estimatedMinutes: 20 });
      expect(isDraftComplete(draft)).toBe(true);
    });
  });
});
