import { describe, expect, it } from "vitest";
import { parseJapaneseBatch, suggestBatchMinutes } from "./batch";

describe("Japanese batch capture", () => {
  it("deduplicates and bounds a 500-item paste without splitting Japanese phrases on spaces", () => {
    const raw = Array.from({ length: 500 }, (_, index) => `${index + 1}. 言葉 ${index}`).concat("言葉 1").join("\n");
    const items = parseJapaneseBatch(raw);
    expect(items).toHaveLength(500);
    expect(items[0]).toBe("言葉 0");
  });

  it("produces a visible, bounded study-minute suggestion", () => {
    expect(suggestBatchMinutes(0)).toBe(0);
    expect(suggestBatchMinutes(500)).toBe(250);
    expect(suggestBatchMinutes(5000)).toBe(360);
  });
});
