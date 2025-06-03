import { defineStore } from "pinia";
import { useApiClient } from "#imports";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null as any,
    isAuthenticated: false,
  }),

  actions: {
    async getUser() {
      try {
        const client = useApiClient();
        const response = await client('/auth/users/me');
        this.user = response;
        this.isAuthenticated = true;
        return response;
      } catch (error) {
        this.user = null;
        this.isAuthenticated = false;
        throw error;
      }
    },

    async login(credentials: { username: string; password: string }) {
      try {
        const client = useApiClient();
        const response: any = await client('/auth/jwt/create', {
          method: 'POST',
          body: credentials
        });

        // Store tokens in localStorage
        localStorage.setItem('token', response.access);
        localStorage.setItem('refresh', response.refresh);

        this.isAuthenticated = true;
        await this.getUser();

        return response;
      } catch (error) {
        this.isAuthenticated = false;
        throw error;
      }
    },

    logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('refresh');
      this.user = null;
      this.isAuthenticated = false;
    }
  }
});
