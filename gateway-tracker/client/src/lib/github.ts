/* Swiss Training Ledger: serialized GitHub backup flow that appends immutable snapshots before updating the latest file. */

import { TrackerStore } from "./tracker";
export interface GitHubConfig { owner: string; repo: string; token: string; branch: string; baseBranch: string; createPullRequest: boolean; }
const API = "https://api.github.com";
async function request(path: string, config: GitHubConfig, init: RequestInit = {}) { const response = await fetch(`${API}${path}`, { ...init, headers: { Accept: "application/vnd.github+json", Authorization: `Bearer ${config.token}`, "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/json", ...(init.headers || {}) } }); const data = await response.json().catch(() => ({})); if (!response.ok) throw new Error(data.message || `GitHub request failed (${response.status})`); return data; }
const b64 = (value: string) => btoa(unescape(encodeURIComponent(value)));

export async function syncToGitHub(store: TrackerStore, config: GitHubConfig) {
  if (!config.owner || !config.repo || !config.token) throw new Error("Isi owner, repo, dan token GitHub terlebih dahulu.");
  const repoPath = `/repos/${encodeURIComponent(config.owner)}/${encodeURIComponent(config.repo)}`;
  const branch = config.branch || "gateway-tracker-sync";
  const baseBranch = config.baseBranch || "main";
  const latestRef = await request(`${repoPath}/git/ref/heads/${encodeURIComponent(baseBranch)}`, config);
  try { await request(`${repoPath}/git/ref`, config, { method: "POST", body: JSON.stringify({ ref: `refs/heads/${branch}`, sha: latestRef.object.sha }) }); } catch (error) { if (!(error instanceof Error) || !error.message.toLowerCase().includes("reference already exists")) throw error; }
  const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
  const latestPath = "data/gateway-tracker-latest.json";
  const journalPath = `data/journal/${timestamp}.json`;
  const content = JSON.stringify(store, null, 2);
  const writeFile = async (path: string, message: string, body: string) => { let sha: string | undefined; try { const existing = await request(`${repoPath}/contents/${path}?ref=${encodeURIComponent(branch)}`, config); sha = existing.sha; } catch { /* New immutable journal file has no SHA. */ } return request(`${repoPath}/contents/${path}`, config, { method: "PUT", body: JSON.stringify({ message, content: b64(body), branch, ...(sha ? { sha } : {}) }) }); };
  await writeFile(journalPath, `tracker: append snapshot ${timestamp}`, content); await writeFile(latestPath, `tracker: update latest snapshot ${timestamp}`, content);
  let pullRequestUrl = "";
  if (config.createPullRequest) { const prs = await request(`${repoPath}/pulls?state=open&head=${encodeURIComponent(`${config.owner}:${branch}`)}&base=${encodeURIComponent(baseBranch)}`, config); if (prs[0]?.html_url) pullRequestUrl = prs[0].html_url; else { const pr = await request(`${repoPath}/pulls`, config, { method: "POST", body: JSON.stringify({ title: "Gateway Tracker sync", head: branch, base: baseBranch, body: "Automated personal progress snapshot from Gateway Tracker. The immutable journal file preserves each sync." }) }); pullRequestUrl = pr.html_url || ""; } }
  return { branch, pullRequestUrl, timestamp };
}
