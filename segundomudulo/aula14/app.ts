import express, { Request, Response, NextFunction } from 'express';
import { authRouter } from './routes/authRoutes';
import { errorHandler } from './middlewares/errorHandler';

const app = express();
app.use(express.json());

app.get('/', (req: Request, res: Response) => {
  res.json({ message: 'Aula 14 auth + error handling' });
});

app.use('/auth', authRoutes);
app.use(errorHandler);

const port = 3004;
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
