require([
    'durandal/app',
    'durandal/system',
], function(app, system) {
    system.debug(true);

    app.configurePlugins({
        router: true,
        dialog: true,
    });

    app.title = 'Dalandan: A Web Application based on DurandalJS';

    app.start().then(function() {
        app.setRoot('shell', 'entrance');
    });
});