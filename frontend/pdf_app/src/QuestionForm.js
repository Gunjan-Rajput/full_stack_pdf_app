import React, { useState } from 'react';
import axios from 'axios';

const QuestionForm = () => {
    const [documentId, setDocumentId] = useState('');
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/ask', {
                document_id: documentId,
                question,
            });
            setAnswer(response.data.answer);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={documentId}
                    onChange={(e) => setDocumentId(e.target.value)}
                    placeholder="Document ID"
                />
                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="Ask a question"
                />
                <button type="submit">Ask</button>
            </form>
            {answer && <p>Answer: {answer}</p>}
        </div>
    );
};

export default QuestionForm;
