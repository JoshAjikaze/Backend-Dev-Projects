import express from 'express';
import dotenv from 'dotenv';

// routes imports
import movieRoutes from './routes/movieRoutes.js'

dotenv.config();
const PORT = process.env.port || 5000

const app = express()
app.use(express.json())

app.use("/movies", movieRoutes)

const server = app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`)
})