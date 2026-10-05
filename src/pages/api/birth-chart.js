import { spawnSync } from "node:child_process";

export async function GET({ url }) {
  const params = url.searchParams;

  const birthDate = params.get("birthDate");
  const birthTime = params.get("birthTime");
  const timezone = params.get("timezone");
  const latitude = params.get("latitude");
  const longitude = params.get("longitude");

  if (
    !birthDate ||
    !birthTime ||
    !timezone ||
    !latitude ||
    !longitude
  ) {
    return new Response(
      JSON.stringify({
        ok: false,
        error: "Missing birth chart parameters"
      }),
      {
        status: 400,
        headers: {
          "Content-Type": "application/json"
        }
      }
    );
  }

  const [year, month, day] = birthDate.split("-").map(Number);
  const [hour, minute] = birthTime.split(":").map(Number);

  const pythonCode = `
from birth_chart import calculate_birth_chart_local
from interpretation import build_cosmic_story
import json
import sys

chart = calculate_birth_chart_local(
    ${year},
    ${month},
    ${day},
    ${hour},
    ${minute},
    ${JSON.stringify(timezone)},
    ${Number(latitude)},
    ${Number(longitude)}
)

interpretation = build_cosmic_story(chart)

result = {
    "chart": chart,
    "interpretation": interpretation
}

sys.stdout.reconfigure(encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
`;

  const result = spawnSync(
    "py",
    [
      "-3.11",
      "-c",
      pythonCode
    ],
    {
      encoding: "utf8"
    }
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

  try {
    const data = JSON.parse(result.stdout);

    return new Response(
      JSON.stringify({
        ok: true,
        chart: data.chart,
        interpretation: data.interpretation
      }),
      {
        headers: {
          "Content-Type": "application/json"
        }
      }
    );
  } catch {
    return new Response(
      JSON.stringify({
        ok: false,
        error: "Invalid response from birth chart engine"
      }),
      {
        status: 500,
        headers: {
          "Content-Type": "application/json"
        }
      }
    );
  }
}