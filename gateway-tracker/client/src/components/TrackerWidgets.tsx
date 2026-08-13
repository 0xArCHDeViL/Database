/* Swiss Training Ledger: reusable data widgets preserve the editorial hierarchy across dashboard sections. */

import { Activity, Dumbbell, Languages, Timer, TrendingUp } from "lucide-react";
import { getLog, getStats, TrackerStore, totalMinutes } from "@/lib/tracker";

export function StatCard({ label, value, note, accent = "ink", icon: Icon }: { label: string; value: string; note: string; accent?: "ink" | "red" | "moss" | "blue"; icon: typeof Activity }) {
  return <div className={`stat-card stat-${accent}`}><div className="stat-top"><span className="eyebrow">{label}</span><Icon size={16} /></div><strong>{value}</strong><span className="stat-note">{note}</span></div>;
}

export function SectionHeading({ index, eyebrow, title, detail, action }: { index: string; eyebrow: string; title: string; detail: string; action?: React.ReactNode }) {
  return <div className="section-heading"><div className="section-index">{index}</div><div><span className="eyebrow">{eyebrow}</span><h2>{title}</h2><p>{detail}</p></div>{action && <div className="section-action">{action}</div>}</div>;
}

export function Heatmap({ store }: { store: TrackerStore }) {
  const days = Array.from({ length: 84 }, (_, index) => { const date = new Date(); date.setDate(date.getDate() - (83 - index)); return date.toISOString().slice(0, 10); });
  const max = Math.max(1, ...days.map((date) => totalMinutes(store.logs[date] || getLog(store, date))));
  return <div className="heatmap-wrap"><div className="heatmap-labels"><span>MINUTES / DAY</span><span>Last 12 weeks</span></div><div className="heatmap">{days.map((date) => { const minutes = totalMinutes(store.logs[date] || getLog(store, date)); const level = minutes === 0 ? 0 : Math.min(4, Math.ceil((minutes / max) * 4)); return <span key={date} className={`heat-cell level-${level}`} title={`${date} · ${minutes} min`} />; })}</div><div className="heat-legend"><span>Less</span>{[0, 1, 2, 3, 4].map((level) => <span key={level} className={`heat-cell level-${level}`} />)}<span>More</span></div></div>;
}

export function CategoryBars({ stats }: { stats: ReturnType<typeof getStats> }) {
  const entries = [{ key: "kotoba", label: "Kotoba", color: "#E84C3D" }, { key: "kanji", label: "Kanji", color: "#A8B78D" }, { key: "bunpou", label: "Bunpou", color: "#8AAEB9" }, { key: "workout", label: "Workout", color: "#20221F" }] as const;
  const max = Math.max(1, ...entries.map((item) => stats.byCategory[item.key]));
  return <div className="category-bars">{entries.map((item) => <div className="category-row" key={item.key}><div className="category-name"><span style={{ background: item.color }} /><b>{item.label}</b><small>{stats.byCategory[item.key]} min</small></div><div className="bar-track"><div className="bar-fill" style={{ width: `${(stats.byCategory[item.key] / max) * 100}%`, background: item.color }} /></div></div>)}</div>;
}

export function ProgressLine({ store }: { store: TrackerStore }) {
  const data = Array.from({ length: 14 }, (_, index) => { const date = new Date(); date.setDate(date.getDate() - (13 - index)); const key = date.toISOString().slice(0, 10); return { key, value: totalMinutes(store.logs[key] || getLog(store, key)) }; });
  const max = Math.max(60, ...data.map((item) => item.value));
  const points = data.map((item, index) => `${(index / 13) * 100},${100 - (item.value / max) * 86 - 7}`).join(" ");
  return <div className="line-chart"><svg viewBox="0 0 100 100" preserveAspectRatio="none" role="img" aria-label="Daily minutes progress"><defs><linearGradient id="lineArea" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stopColor="#E84C3D" stopOpacity=".28" /><stop offset="1" stopColor="#E84C3D" stopOpacity="0" /></linearGradient></defs><polyline points={`0,100 ${points} 100,100`} fill="url(#lineArea)" stroke="none" /><polyline points={points} fill="none" stroke="#E84C3D" strokeWidth="1.8" vectorEffect="non-scaling-stroke" strokeLinecap="round" strokeLinejoin="round" />{data.map((item, index) => <circle key={item.key} cx={(index / 13) * 100} cy={100 - (item.value / max) * 86 - 7} r="1.5" fill="#F4F0E8" stroke="#E84C3D" strokeWidth="1" vectorEffect="non-scaling-stroke"><title>{item.key}: {item.value} min</title></circle>)}</svg><div className="chart-axis"><span>{data[0].key.slice(5)}</span><span>Today / {data[13].value} min</span></div></div>;
}
