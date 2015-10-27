define([
    'knockout'
], function(ko) {
    return {
        title: ko.observable(),

        todos: ko.observableArray([
            { id: 1, title: 'Todo 1', done: ko.observable(false) },
            { id: 2, title: 'Todo 2', done: ko.observable(false) },
            { id: 3, title: 'Todo 3', done: ko.observable(false) },
        ]),

        create: function() {
            var title = this.title();

            if (title) {
                this.todos.push({ id: Math.floor(Math.random() * (999 - 4 + 1)) + 4, title: title, done: ko.observable(false) });
            }

            // Clear
            this.title('');
        },
    };
});