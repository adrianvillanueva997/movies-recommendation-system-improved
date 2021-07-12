import express, { Request, Response } from "express";
import dotenv from "dotenv";
import promBundle from "express-prom-bundle";

import { health } from "./routes/health/health";
import { movies } from "./routes/movies/movies";

const metricsMiddleware = promBundle({ includeMethod: true });
const app = express();
dotenv.config();

app.use(express.json());
app.use(metricsMiddleware);
app.use(health);
app.use(movies);

app.listen("3000", () => {
  console.log("Server running!");
});

app.get("/", (req: Request, res: Response) => {
  res.send("hello world!");
});
