import express from 'express';
import * as WebSocket from 'ws';
import { createServer } from 'http';
import dotenv from 'dotenv';
import { handleMessage } from './controller';

// Load environment variables from .env file
dotenv.config();
const PORT = process.env.EXPRESS_PORT || 5050;

// Initialize application
const app = express();
const server = createServer(app);

// WebSocket Server
const wss = new WebSocket.Server({ server });

wss.on('connection', (ws: WebSocket) => {
    console.log('A new client Connected');
    
    ws.on('message', (message) => {
        handleMessage(ws, message);
    });
});

// Express Server

server.listen(PORT, () => {
    console.log(`Server started on port ${PORT}.`);
});
