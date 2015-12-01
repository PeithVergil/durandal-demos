define([
    'jquery',
    'knockout',
    'todo/Todo',
], function($, ko, Todo) {
    var STATUS_OPEN = 1;
    var STATUS_DONE = 2;

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

    TodoClient.prototype.setStatus = function(todo, status) {
        switch (status) {
            case 'open':
                var data = {
                    status: STATUS_OPEN
                };
                break;
            
            case 'done':
                var data = {
                    status: STATUS_DONE
                };
                break;
        }

        var $request = $.ajax({ type: 'PATCH', data: data, url: '/api/v1/todos/' + todo.id + '/update/' });

        $request.done(function(result) {
            switch (result.status) {
                case STATUS_OPEN:
                    todo.done(false); break;
                
                case STATUS_DONE:
                    todo.done(true); break;
            }
        });
    };

    return new TodoClient();
});