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

app.use("/movies", movieRoutes)

const server = app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`)
})

// process.on("unhandledRejection", (err) => {
//     console.error("Unhandled Rejection:", err);
// })