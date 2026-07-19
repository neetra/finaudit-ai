-- 1. Create the table
CREATE TABLE transaction_embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    transaction_id UUID NOT NULL REFERENCES transactions(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT NOW(),
    embedding vector(1536) -- For OpenAI text-embedding-3-small
);

-- -- 2. Create an HNSW index for lightning-fast vector search
-- -- (Run this after you have a few hundred rows, it speeds up queries drastically)
-- CREATE INDEX ON transaction_embeddings USING hnsw (embedding vector_cosine_ops);