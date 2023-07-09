import express from 'express';
import { fileURLToPath } from 'url';
import path from 'path';

const app = express();
const port = 3000;

const filename = fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

app.get('/', (_, res) => {
	res.send('Welcome!');
});

app.get('/files/:file', async (req, res) => {
	const { file } = req.params;
	const filePath = path.resolve(dirname, 'files', file);
	res.sendFile(filePath);
});

app.listen(port, () => console.log(`Listening on port ${port}...`));
