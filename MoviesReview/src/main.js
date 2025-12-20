import express from 'express';
import dotenv from 'dotenv';
import { connectDB, disconnectDB } from './config/db.js';

// routes imports
import movieRoutes from './routes/movieRoutes.js'

dotenv.config();
// connectDB()


const PORT = process.env.PORT || 5001

const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }));

app.use("/movies", movieRoutes)

const server = app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`)
})

process.on("unhandledRejection", (err) => {
    console.error("Unhandled Rejection:", err);
    server.close(async () => {
        await disconnectDB();
        process.exit(1);
    });
});

// Handle uncaught exceptions
process.on("uncaughtException", async (err) => {
    console.error("Uncaught Exception:", err);
    await disconnectDB();
    process.exit(1);
});

// Graceful shutdown
process.on("SIGTERM", async () => {
    console.log("SIGTERM received, shutting down gracefully");
    server.close(async () => {
        await disconnectDB();
        process.exit(0);
    });
});