define([
    'knockout',
    'todo/Todo',
    'todo/TodoClient',
], function(ko, Todo, TodoClient) {
    var todos = ko.observableArray();

    TodoClient.list(function(results) {
        ko.utils.arrayForEach(results, function(result) {
            todos.push(result);
        });
    });
    
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
            TodoClient.delete(todo, function() {
                todos.remove(todo);
            });
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

        checked: function(todo, event) {
            if (todo.done())
                TodoClient.setStatus(todo, 'done');
            else
                TodoClient.setStatus(todo, 'open');

            return true;
        },
    };
});