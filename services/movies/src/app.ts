import express, { Request, Response } from "express";
import dotenv from "dotenv";
import promBundle from "express-prom-bundle";
const metricsMiddleware = promBundle({ includeMethod: true });

import { health } from "./routes/health";

const app = express();
app.use(express.json());
app.use(metricsMiddleware);
app.use(health);

app.listen("3000", () => {
  console.log("Server running!");
});

app.get("/", (req: Request, res: Response) => {
  res.send("hello world!");
});
