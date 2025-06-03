export function useApiClient() {
    const config = useRuntimeConfig();
  
    return $fetch.create({
      baseURL: config.public.apiBase,
      onRequest({ options }) {
        const token = localStorage.getItem('token');
  
        options.headers = {
          ...options.headers,
          ...(token ? { Authorization: `JWT ${token}` } : {}),
        };
      },
      onResponseError({ response }) {
        if (response.status === 401) {
          const authStore = useAuthStore();
          authStore.logout(); // Clear everything
        }
      }
    });
  }
  