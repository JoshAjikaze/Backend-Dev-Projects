import express from 'express';

const movieRoute = express.Router();

const movies = [
    { id: "1", title: "Sample title 1", duration: "60", noOfLikes: "10" },
    { id: "2", title: "Sample title 2", duration: "12", noOfLikes: "17" },
    { id: "3", title: "Sample title 3", duration: "74", noOfLikes: "2" },
    { id: "4", title: "Sample title 4", duration: "65", noOfLikes: "0" },
]

movieRoute.get('/', (req, res) => {
    res.status(200).json({ movies: movies });
});

movieRoute.get('/:id', (req, res) => {
    const { id } = req.params
    const movieIndex = movies.findIndex((movie) => movie.id === id)
    res.status(200).json({ movie: movies[movieIndex] });
});

movieRoute.post('/', (req, res) => {
    const { id, title, duration, noOfLikes } = req.body;

    // Validate required fields
    if (!id || !title || !duration || noOfLikes === undefined) {
        return res.status(400).json({ error: 'Missing required fields: id, title, duration, noOfLikes' });
    }

    // Check if movie with same id already exists
    if (movies.some((movie) => movie.id === id)) {
        return res.status(409).json({ error: 'Movie with this id already exists' });
    }

    movies.push(req.body);
    res.status(201).json({ message: 'Movie added', movies: movies })
});

movieRoute.put('/', (req, res) => {
    res.send('Edit a movie');
});

movieRoute.delete('/:id', (req, res) => {
    const { id } = req.params;
    const movieIndex = movies.findIndex((movie) => movie.id === id);

    if (movieIndex === -1) {
        return res.status(404).json({ error: 'Movie not found' });
    }

    movies.splice(movieIndex, 1);
    res.status(200).json({ message: 'Movie deleted', movies: movies });
});



export default movieRoute;