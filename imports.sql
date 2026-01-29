--
-- PostgreSQL database dump
--

\restrict u2mndd5SuWlJ9jhJwTauxCXmJiHoBfocU0r16sgriiPPv3RaRFr4VwXYT3xbM98

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

-- Started on 2026-01-29 20:01:07

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4881 (class 1262 OID 18568)
-- Name: imports; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE imports WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'German_Germany.1252';


ALTER DATABASE imports OWNER TO postgres;

\unrestrict u2mndd5SuWlJ9jhJwTauxCXmJiHoBfocU0r16sgriiPPv3RaRFr4VwXYT3xbM98
\connect imports
\restrict u2mndd5SuWlJ9jhJwTauxCXmJiHoBfocU0r16sgriiPPv3RaRFr4VwXYT3xbM98

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 18576)
-- Name: dim_countries; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dim_countries (
    country_id integer NOT NULL,
    country_name text NOT NULL
);


ALTER TABLE public.dim_countries OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 18585)
-- Name: dim_products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dim_products (
    hs_code integer NOT NULL,
    product_name text NOT NULL
);


ALTER TABLE public.dim_products OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 18569)
-- Name: dim_years; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dim_years (
    year_id integer NOT NULL,
    year integer NOT NULL
);


ALTER TABLE public.dim_years OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 18617)
-- Name: fact_imports; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fact_imports (
    import_id integer NOT NULL,
    year_id integer NOT NULL,
    country_id integer NOT NULL,
    hs_code integer NOT NULL,
    quantity numeric,
    netweight numeric,
    price numeric
);


ALTER TABLE public.fact_imports OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 18616)
-- Name: fact_imports_import_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fact_imports_import_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.fact_imports_import_id_seq OWNER TO postgres;

--
-- TOC entry 4882 (class 0 OID 0)
-- Dependencies: 220
-- Name: fact_imports_import_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fact_imports_import_id_seq OWNED BY public.fact_imports.import_id;


--
-- TOC entry 223 (class 1259 OID 18641)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password_hash text NOT NULL,
    created_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 18640)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- TOC entry 4883 (class 0 OID 0)
-- Dependencies: 222
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 4707 (class 2604 OID 18620)
-- Name: fact_imports import_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_imports ALTER COLUMN import_id SET DEFAULT nextval('public.fact_imports_import_id_seq'::regclass);


--
-- TOC entry 4708 (class 2604 OID 18644)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 4715 (class 2606 OID 18584)
-- Name: dim_countries dim_countries_country_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dim_countries
    ADD CONSTRAINT dim_countries_country_name_key UNIQUE (country_name);


--
-- TOC entry 4717 (class 2606 OID 18582)
-- Name: dim_countries dim_countries_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dim_countries
    ADD CONSTRAINT dim_countries_pkey PRIMARY KEY (country_id);


--
-- TOC entry 4719 (class 2606 OID 18591)
-- Name: dim_products dim_products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dim_products
    ADD CONSTRAINT dim_products_pkey PRIMARY KEY (hs_code);


--
-- TOC entry 4711 (class 2606 OID 18573)
-- Name: dim_years dim_years_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dim_years
    ADD CONSTRAINT dim_years_pkey PRIMARY KEY (year_id);


--
-- TOC entry 4713 (class 2606 OID 18575)
-- Name: dim_years dim_years_year_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dim_years
    ADD CONSTRAINT dim_years_year_key UNIQUE (year);


--
-- TOC entry 4721 (class 2606 OID 18624)
-- Name: fact_imports fact_imports_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_imports
    ADD CONSTRAINT fact_imports_pkey PRIMARY KEY (import_id);


--
-- TOC entry 4723 (class 2606 OID 18653)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 4725 (class 2606 OID 18649)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 4727 (class 2606 OID 18651)
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- TOC entry 4728 (class 2606 OID 18630)
-- Name: fact_imports fact_imports_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_imports
    ADD CONSTRAINT fact_imports_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.dim_countries(country_id);


--
-- TOC entry 4729 (class 2606 OID 18635)
-- Name: fact_imports fact_imports_hs_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_imports
    ADD CONSTRAINT fact_imports_hs_code_fkey FOREIGN KEY (hs_code) REFERENCES public.dim_products(hs_code);


--
-- TOC entry 4730 (class 2606 OID 18625)
-- Name: fact_imports fact_imports_year_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_imports
    ADD CONSTRAINT fact_imports_year_id_fkey FOREIGN KEY (year_id) REFERENCES public.dim_years(year_id);


-- Completed on 2026-01-29 20:01:07

--
-- PostgreSQL database dump complete
--

\unrestrict u2mndd5SuWlJ9jhJwTauxCXmJiHoBfocU0r16sgriiPPv3RaRFr4VwXYT3xbM98

