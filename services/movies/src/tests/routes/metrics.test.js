const http = require("http");

describe("Health endpoint", () => {
  it("/metrics", async () => {
    const res = await http.get("http://localhost:3000/metrics", (resp) => {
      expect(resp.statusCode).toEqual(200);
    });
  });
});
