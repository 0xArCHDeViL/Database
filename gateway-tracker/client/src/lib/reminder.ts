export type NotificationStatus = "unsupported" | "default" | "granted" | "denied";

export function notificationStatus(): NotificationStatus {
  if (typeof window === "undefined" || !("Notification" in window)) return "unsupported";
  return Notification.permission;
}

export async function requestReminderPermission(): Promise<NotificationStatus> {
  if (notificationStatus() === "unsupported") return "unsupported";
  if (Notification.permission === "default") await Notification.requestPermission();
  return notificationStatus();
}

export function alarmEndTime(blockMinutes: number, now = Date.now()): number {
  const safeMinutes = Math.max(1, Math.min(180, Math.round(Number(blockMinutes) || 0)));
  return now + safeMinutes * 60_000;
}

export function remainingAlarmSeconds(endsAt: number, now = Date.now()): number {
  return Math.max(0, Math.ceil((endsAt - now) / 1000));
}

export function formatAlarmCountdown(seconds: number): string {
  const safe = Math.max(0, Math.round(seconds));
  return `${String(Math.floor(safe / 60)).padStart(2, "0")}:${String(safe % 60).padStart(2, "0")}`;
}

export function fireReminder(title: string, body: string): "notification" | "fallback" {
  if (notificationStatus() === "granted") {
    new Notification(title, { body, tag: "gateway-focus-alarm" });
    return "notification";
  }
  return "fallback";
}

function jakartaClock(now: Date) {
  const parts = new Intl.DateTimeFormat("en-GB", { timeZone: "Asia/Jakarta", hour: "2-digit", minute: "2-digit", hour12: false, year: "numeric", month: "2-digit", day: "2-digit" }).formatToParts(now);
  const part = (type: Intl.DateTimeFormatPartTypes) => parts.find((item) => item.type === type)?.value ?? "00";
  return { date: `${part("year")}-${part("month")}-${part("day")}`, minutes: Number(part("hour")) * 60 + Number(part("minute")) };
}

export function shouldFireDailyReminder(reminderTime: string, lastFiredDate: string | null, now = new Date()): { due: boolean; date: string } {
  const clock = jakartaClock(now);
  const [hour, minute] = reminderTime.split(":").map(Number);
  const target = Number.isFinite(hour) && Number.isFinite(minute) ? hour * 60 + minute : 19 * 60 + 30;
  return { date: clock.date, due: clock.minutes >= target && lastFiredDate !== clock.date };
}
