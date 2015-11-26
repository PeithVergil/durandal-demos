define([
    'knockout'
], function(ko) {
    var todos = ko.observableArray([
        { id: 1, title: ko.observable('Todo 1'), done: ko.observable(false), edit: ko.observable(false) },
        { id: 2, title: ko.observable('Todo 2'), done: ko.observable(false), edit: ko.observable(false) },
        { id: 3, title: ko.observable('Todo 3'), done: ko.observable(false), edit: ko.observable(false) },
    ]);
    
    return {
        todos: todos,
        
        title: ko.observable(),

        create: function() {
            var title = this.title();

            if (title) {
                todos.push({
                    id    : Math.floor(Math.random() * (999 - 4 + 1)) + 4,
                    title : ko.observable(title),
                    done  : ko.observable(false),
                    edit  : ko.observable(false)
                });
            }

            // Clear
            this.title('');
        },

        update: function(todo) {
            todo.edit(!todo.edit());
        },

        delete: function(todo) {
            todos.remove(todo);
        },
    };
});