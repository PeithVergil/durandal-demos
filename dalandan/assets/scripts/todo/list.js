define([
    'knockout',
    'todo/Todo',
    'todo/TodoClient',
], function(ko, Todo, TodoClient) {
    var todos = ko.observableArray([
        new Todo(1, 'Todo 1'),
        new Todo(2, 'Todo 2'),
        new Todo(3, 'Todo 3'),
    ]);
    
    return {
        todos: todos,
        
        title: ko.observable(),

        create: function() {
            var title = this.title();

            if (title) {
                var data = {
                    title: title
                };

                TodoClient.create(data, function(todo) {
                    todos.push(todo);
                });
            }

            // Clear form.
            this.title('');
        },

        update: function(todo) {
            todo.edit(!todo.edit());
        },

        delete: function(todo) {
            todos.remove(todo);
        },

        updateSubmit: function(todo) {
            // Update title to new value.
            todo.title(todo.draft());

            // Stop edit mode.
            todo.edit(false);
        },
        
        updateCancel: function(todo, event) {
            switch (event.keyCode) {
                // ESCAPE to cancel.
                case 27:
                    // Revert draft to old value.
                    todo.draft(todo.title());

                    // Stop edit mode.
                    todo.edit(false);

                    break;

                default:
                    // Handle default behavior.
                    return true;
            }
        },
    };
});