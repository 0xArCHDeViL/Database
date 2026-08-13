import { describe, expect, it } from "vitest";
import { alarmEndTime, formatAlarmCountdown, remainingAlarmSeconds, shouldFireDailyReminder } from "./reminder";

describe("local focus reminder", () => {
  it("creates a bounded end time and a stable countdown", () => {
    const now = 1_000_000;
    const endsAt = alarmEndTime(25, now);
    expect(endsAt).toBe(now + 1_500_000);
    expect(remainingAlarmSeconds(endsAt, now + 60_000)).toBe(1440);
    expect(formatAlarmCountdown(1440)).toBe("24:00");
  });

  it("fires a local daily reminder once the Jakarta schedule is reached, once per date", () => {
    const now = new Date("2026-08-14T12:40:00.000Z"); // 19:40 Jakarta
    const first = shouldFireDailyReminder("19:30", null, now);
    expect(first).toEqual({ due: true, date: "2026-08-14" });
    expect(shouldFireDailyReminder("19:30", first.date, now).due).toBe(false);
  });
});
