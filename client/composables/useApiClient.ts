export function useApiClient() {
    const config = useRuntimeConfig();
    const token = useCookie('token');

    return $fetch.create({
        baseURL: config.public.apiBase as string,
        onRequest({ request, options }) {
            options.headers = {
                ...(options.headers || {}),
                ...(token?.value ? { Authorization: `Bearer ${token.value}` } : {}),
            };
        }        
    });
}
