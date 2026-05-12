-- Table pour stocker toutes les phrases officielles de l'application
CREATE TABLE IF NOT EXISTS public.phrases (
    id SERIAL PRIMARY KEY,
    theme VARCHAR(50) NOT NULL, -- 'soft' ou 'hard'
    game_mode VARCHAR(50) NOT NULL, -- 'tribunal', 'boire_action', etc.
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Table pour le contenu généré par les utilisateurs (UGC)
CREATE TABLE IF NOT EXISTS public.pending_phrases (
    id SERIAL PRIMARY KEY,
    theme VARCHAR(50) NOT NULL,
    game_mode VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    submitted_by VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Activer Row Level Security (RLS)
ALTER TABLE public.phrases ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.pending_phrases ENABLE ROW LEVEL SECURITY;

-- Autoriser la LECTURE publique sur les phrases (tout le monde peut télécharger les phrases)
CREATE POLICY "Allow public read access on phrases" 
ON public.phrases FOR SELECT 
USING (true);

-- Autoriser l'INSERTION publique sur les pending_phrases (tout le monde peut soumettre)
CREATE POLICY "Allow public insert on pending_phrases" 
ON public.pending_phrases FOR INSERT 
WITH CHECK (true);

-- (Optionnel) Bloquer la lecture publique des phrases en attente
CREATE POLICY "Deny public read on pending_phrases" 
ON public.pending_phrases FOR SELECT 
USING (false);
