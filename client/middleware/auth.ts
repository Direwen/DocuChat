export default defineNuxtRouteMiddleware((to, from) => {

    if (localStorage.getItem('token') && to.path.startsWith('/auth')) {
        console.log("Redirecting authenticated user from auth page");
        return navigateTo('/');
    }

});