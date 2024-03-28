import { ConversationRequest, ConversationResponse, SMmessage } from 'interfaces';
import * as WebSocket from 'ws';

export function handleMessage(ws: WebSocket, message: any) {
    try {
        const msg: SMmessage = JSON.parse(message);
        if (msg.name == 'conversationRequest') {
            let request: ConversationRequest = msg.body as ConversationRequest;
            handleRequest(ws, request);
        }
    } catch {
        console.log('Unrecognized message: ', message);
    }
}

export function handleRequest(ws: WebSocket, req: ConversationRequest) {
    console.log('Conv request: ', req);

    // Set a simple response
    let resp : ConversationResponse = {
        input: { text: req.input.text },
        // output: { text: `Echo: ${req.input.text}` },
        output: { text: ` Hi there nice looking new person #Wave I've always wanted to meet! Oh my gosh it's so exciting to finally meet you! Oh wow, wow, wow! You're amazing. Can I get your autograph? Please please please!!!! Stop sleep` },
        variables: {}
    };

    // Handle welcome message
    if (req.optionalArgs?.kind == 'init') {
        resp.output.text = '#EnableStopTalkingGesture Hi there, everyone! #Wave ';
    }

    // Set fallback response example (can be handled by skills in the project)
    if (req.input.text.toLowerCase().startsWith('why')) {
        resp.output.text = 'I do not know how to answer that';
        resp.fallback = true;
    }

    // SM content cards example
    if (req.input.text.toLowerCase() == 'show card') {
        resp.output.text = 'Here is a cat @showcards(cat)';
        resp.variables['public-cat'] = {
            'component': 'image',
            'data': {
                'alt': 'A cute kitten',
                'url': 'https://placekitten.com/300/300'
            }
        };
    }

    sendMessage(ws, resp);
}

function sendMessage(ws: WebSocket, resp: ConversationResponse) {
    let message: SMmessage = {
        category: 'scene',
        kind: 'request',
        name: 'conversationResponse',
        body: resp
    };

    ws.send(JSON.stringify(message));
}
