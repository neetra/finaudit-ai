CREATE OR REPLACE FUNCTION create_user(p_email TEXT, p_name TEXT, p_password TEXT)
RETURNS UUID
LANGUAGE plpgsql
AS $$
DECLARE
    v_user_id UUID;
BEGIN
    INSERT INTO users (email, name, password)
    VALUES (p_email, p_name, p_password)
    RETURNING id INTO v_user_id;

    RETURN v_user_id;
END;
$$;
