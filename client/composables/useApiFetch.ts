import { useFetch } from "#app";

export function useApiFetch<T>(path: string, options = {}) {
    const config = useRuntimeConfig();
    const token = useCookie('token') ?? null;

    return useFetch<T>(`${config.public.apiBase}${path}`, {
        ...options,
        headers: {
            ...(options as any).headers,
            ...(token?.value ? { Authorization: `Bearer ${token.value}` } : {})
        }
    });
}