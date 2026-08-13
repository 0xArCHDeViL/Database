/* Swiss Training Ledger: deterministic workbook export with summary, daily, Japanese, and workout sheets. */

import { DailyLog, TrackerStore, formatDate, getStats, japaneseMinutes, rangeDates, totalMinutes, typeLabel, workoutMinutes } from "./tracker";

const headerStyle = { font: { bold: true, color: "FFFFFF" }, fill: { fgColor: { rgb: "20221F" } }, alignment: { vertical: "center" } };
const accentStyle = { font: { bold: true, color: "FFFFFF" }, fill: { fgColor: { rgb: "E84C3D" } }, alignment: { vertical: "center" } };
type Sheet = import("xlsx").WorkSheet;
type SheetUtils = typeof import("xlsx")["utils"];
function styleHeader(sheet: Sheet, row: number, utils: SheetUtils, style = headerStyle) { const range = utils.decode_range(sheet["!ref"] || "A1:A1"); for (let c = range.s.c; c <= range.e.c; c += 1) { const cell = sheet[utils.encode_cell({ r: row, c })]; if (cell) cell.s = style; } }
function finishSheet(sheet: Sheet, widths: number[]) { sheet["!cols"] = widths.map((wch) => ({ wch })); sheet["!freeze"] = { xSplit: 0, ySplit: 1 }; }

export function buildExportRows(store: TrackerStore, from: string, to: string) {
  const dates = rangeDates(from, to);
  const logs = dates.map((date) => store.logs[date]).filter(Boolean) as DailyLog[];
  const stats = getStats(store, from, to);
  return {
    summary: [["GATEWAY TRACKER", "Monthly / custom range export"], ["Range", `${from} → ${to}`], ["Total minutes", stats.totalMinutes], ["Active days", stats.activeDays], ["Japanese items", stats.items], [], ["Category", "Minutes"], ["Kotoba", stats.byCategory.kotoba], ["Kanji", stats.byCategory.kanji], ["Bunpou", stats.byCategory.bunpou], ["Workout", stats.byCategory.workout], [], ["Exported at", new Date().toISOString()]],
    daily: [["Date", "Day", "Total minutes", "Japanese minutes", "Workout minutes", "Free minutes", "Items", "Workout done", "Note"], ...dates.map((date) => { const log = store.logs[date]; return [date, formatDate(date, { weekday: "long" }), log ? totalMinutes(log) : 0, log ? japaneseMinutes(log) : 0, log ? workoutMinutes(log) : 0, log?.freeMinutes ?? 0, log?.japanese.filter((x) => x.content.trim()).length ?? 0, log && (log.workout.ladder || log.workout.cindy) ? "Yes" : "No", log?.note ?? ""]; })],
    japanese: [["Date", "Type", "Content", "Reading / Furigana", "JLPT", "Study minutes", "Example sentence", "Sentence minutes"], ...logs.flatMap((log) => log.japanese.filter((entry) => entry.content.trim()).map((entry) => [log.date, typeLabel[entry.type], entry.content, entry.reading, entry.jlpt, entry.studyMinutes, entry.sentence, entry.sentenceMinutes]))],
    workout: [["Date", "Ladder", "Ladder rounds", "Ladder minutes", "Ladder notes", "Cindy", "Cindy rounds", "Cindy minutes", "Cindy notes"], ...logs.map((log) => [log.date, log.workout.ladder ? "Yes" : "No", log.workout.ladderRounds, log.workout.ladderMinutes, log.workout.ladderNotes, log.workout.cindy ? "Yes" : "No", log.workout.cindyRounds, log.workout.cindyMinutes, log.workout.cindyNotes])],
  };
}

export async function exportWorkbook(store: TrackerStore, from: string, to: string) {
  const XLSX = await import("xlsx");
  const rows = buildExportRows(store, from, to);
  const workbook = XLSX.utils.book_new();
  const summary = XLSX.utils.aoa_to_sheet(rows.summary);
  styleHeader(summary, 0, XLSX.utils, accentStyle); styleHeader(summary, 6, XLSX.utils); finishSheet(summary, [24, 28]); XLSX.utils.book_append_sheet(workbook, summary, "Summary");
  const daily = XLSX.utils.aoa_to_sheet(rows.daily);
  styleHeader(daily, 0, XLSX.utils); finishSheet(daily, [14, 18, 16, 18, 16, 14, 10, 14, 42]); XLSX.utils.book_append_sheet(workbook, daily, "Daily Log");
  const japanese = XLSX.utils.aoa_to_sheet(rows.japanese);
  styleHeader(japanese, 0, XLSX.utils); finishSheet(japanese, [14, 14, 24, 24, 10, 14, 52, 16]); XLSX.utils.book_append_sheet(workbook, japanese, "Japanese Detail");
  const workout = XLSX.utils.aoa_to_sheet(rows.workout);
  styleHeader(workout, 0, XLSX.utils); finishSheet(workout, [14, 12, 14, 16, 34, 12, 14, 16, 34]); XLSX.utils.book_append_sheet(workbook, workout, "Workout Log");
  XLSX.writeFile(workbook, `gateway-tracker_${from}_${to}.xlsx`);
}
