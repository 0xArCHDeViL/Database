/* Swiss Training Ledger: network-free coverage for append-only GitHub backup sequencing. */

import { afterEach, describe, expect, it, vi } from "vitest";
import { syncToGitHub } from "./github";
import { TrackerStore } from "./tracker";

const store: TrackerStore = { version: 1, logs: {} };
const config = { owner: "arch", repo: "gateway-data", token: "token", branch: "gateway-tracker-sync", baseBranch: "main", createPullRequest: true };
const response = (status: number, data: unknown) => new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json" } });

afterEach(() => vi.unstubAllGlobals());

describe("GitHub append-only backup", () => {
  it("continues when the sync branch already exists and updates an existing latest pointer", async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(response(200, { object: { sha: "base-sha" } }))
      .mockResolvedValueOnce(response(422, { message: "Reference already exists" }))
      .mockResolvedValueOnce(response(404, { message: "Not Found" }))
      .mockResolvedValueOnce(response(201, { content: { sha: "journal" } }))
      .mockResolvedValueOnce(response(200, { sha: "latest-sha" }))
      .mockResolvedValueOnce(response(200, { content: { sha: "next-latest" } }))
      .mockResolvedValueOnce(response(200, [{ html_url: "https://github.com/arch/gateway-data/pull/1" }]));
    vi.stubGlobal("fetch", fetchMock);

    const result = await syncToGitHub(store, config);

    expect(result.branch).toBe("gateway-tracker-sync");
    expect(result.pullRequestUrl).toContain("pull/1");
    expect(fetchMock).toHaveBeenCalledTimes(7);
    const latestWrite = JSON.parse(String(fetchMock.mock.calls[5][1].body));
    expect(latestWrite.sha).toBe("latest-sha");
    expect(latestWrite.branch).toBe("gateway-tracker-sync");
  });

  it("refuses to attempt network sync without the required personal fields", async () => {
    await expect(syncToGitHub(store, { ...config, token: "" })).rejects.toThrow("Isi owner");
  });
});
