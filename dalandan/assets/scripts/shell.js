define([
    'plugins/router',
], function(router) {
    return {
        router: router,
        activate: function() {
            router.map([
                { route: '',      moduleId: 'todo/main',  title: 'Todos' },
                { route: 'todo',  moduleId: 'todo/main',  title: 'Todos', nav: true },
                { route: 'about', moduleId: 'about/main', title: 'About', nav: true },
            ]);

            return router.buildNavigationModel().activate();
        },
    };
});