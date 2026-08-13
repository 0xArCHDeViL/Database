/* Swiss Training Ledger: export rows are verified separately from the lazy spreadsheet runtime. */

import { describe, expect, it } from "vitest";
import { buildExportRows } from "./export";
import { TrackerStore } from "./tracker";

describe("workbook row contract", () => {
  it("creates the four stable sheets with blank days and detailed Japanese rows", () => {
    const store: TrackerStore = { version: 1, logs: { "2026-08-13": { date: "2026-08-13", workout: { ladder: false, ladderRounds: 0, ladderMinutes: 0, ladderNotes: "", cindy: true, cindyRounds: 12, cindyMinutes: 20, cindyNotes: "" }, japanese: [{ id: "1", type: "kotoba", content: "覚える", reading: "おぼえる", jlpt: "N3", studyMinutes: 15, sentence: "漢字を覚える。", sentenceMinutes: 5 }], freeMinutes: 20, note: "ok", updatedAt: "2026-08-13T00:00:00.000Z" } } };
    const rows = buildExportRows(store, "2026-08-12", "2026-08-13");
    expect(rows.summary[0]).toEqual(["GATEWAY TRACKER", "Monthly / custom range export"]);
    expect(rows.daily).toHaveLength(3);
    expect(rows.daily[1][2]).toBe(0);
    expect(rows.japanese[1]).toContain("覚える");
    expect(rows.workout[1][5]).toBe("Yes");
  });
});
