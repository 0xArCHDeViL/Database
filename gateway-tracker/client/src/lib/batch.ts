import { JapaneseBatch, JapaneseType, JLPTLevel } from "./tracker";

const MAX_BATCH_ITEMS = 1000;

export function parseJapaneseBatch(raw: string, maxItems = MAX_BATCH_ITEMS): string[] {
  const seen = new Set<string>();
  const result: string[] = [];

  raw
    .replace(/\r/g, "")
    .split(/[\n;,]+/)
    .map((line) => line.replace(/^\s*(?:[-*•] |\d+[.)、]\s*)/, "").trim().slice(0, 160))
    .filter(Boolean)
    .forEach((item) => {
      const key = item.toLocaleLowerCase("ja-JP");
      if (!seen.has(key) && result.length < maxItems) {
        seen.add(key);
        result.push(item);
      }
    });

  return result;
}

export function suggestBatchMinutes(itemCount: number): number {
  if (!Number.isFinite(itemCount) || itemCount <= 0) return 0;
  return Math.max(5, Math.min(360, Math.ceil(itemCount * 0.5)));
}

export function createJapaneseBatch(input: {
  raw: string;
  type: JapaneseType;
  jlpt: JLPTLevel;
  studyMinutes?: number;
  sentenceMinutes?: number;
  note?: string;
}): JapaneseBatch | null {
  const items = parseJapaneseBatch(input.raw);
  if (!items.length) return null;

  return {
    id: crypto.randomUUID(),
    type: input.type,
    jlpt: input.jlpt,
    items,
    studyMinutes: Math.max(0, Math.round(input.studyMinutes ?? suggestBatchMinutes(items.length))),
    sentenceMinutes: Math.max(0, Math.round(input.sentenceMinutes ?? 0)),
    note: (input.note ?? "").trim().slice(0, 300),
    createdAt: new Date().toISOString(),
  };
}
