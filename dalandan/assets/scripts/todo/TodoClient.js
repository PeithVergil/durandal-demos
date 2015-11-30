define([
    'jquery',
    'knockout',
    'todo/Todo',
], function($, ko, Todo) {
    function TodoClient() {
    }

    TodoClient.prototype.create = function(data, callback) {
        var $request = $.post('/api/v1/todos/create/', data);

        $request.done(function(result) {
            var todo = new Todo(result.id, result.title);

            if ((typeof callback) !== 'undefined')
                callback(todo);
        });
    };

    return new TodoClient();
});