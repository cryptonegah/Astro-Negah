import { spawnSync } from "node:child_process";

export async function GET() {
  const result = spawnSync(
    "py",
    [
      "-3.11",
      "-c",
      "from birth_chart import calculate_birth_chart_local; r=calculate_birth_chart_local(2000,1,1,15,30,'Asia/Tehran',35.6892,51.3890); print(r['ascendant_zodiac']['sign'])"
    ],
    { encoding: "utf8" }
  );

  if (result.status !== 0) {
    return new Response(
      JSON.stringify({
        ok: false,
        error: result.stderr
      }),
      {
        status: 500,
        headers: {
          "Content-Type": "application/json"
        }
      }
    );
  }

  return new Response(
    JSON.stringify({
      ok: true,
      ascendant: result.stdout.trim()
    }),
    {
      headers: {
        "Content-Type": "application/json"
      }
    }
  );
}