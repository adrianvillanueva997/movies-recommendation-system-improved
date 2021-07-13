import express, { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();
const router = express.Router();

router.get("/movie", async (req: Request, res: Response) => {
  const movies = await prisma.movie.findMany({
    select: {
      id: true,
      title: true,
      Genres: {
        select: {
          id: true,
          movieId: false,
          Genre: true,
        },
      },
    },
  });
  res.send(movies);
});

export { router as movies };
