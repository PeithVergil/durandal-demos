define([
    'jquery',
    'knockout',
    'todo/Todo',
], function($, ko, Todo) {
    var STATUS_OPEN = 1;
    var STATUS_DONE = 2;

    function TodoClient() {
    }

    TodoClient.prototype.list = function(callback) {
        var $request = $.get('/api/v1/todos/list/');

        $request.done(function(result) {
            var todos = ko.utils.arrayMap(result, function(item) {
                return new Todo(item.id, item.title);
            });

            if ((typeof callback) !== 'undefined')
                callback(todos);
        });
    };

    TodoClient.prototype.create = function(data, callback) {
        var $request = $.post('/api/v1/todos/create/', data);

        $request.done(function(result) {
            var todo = new Todo(result.id, result.title);

            if ((typeof callback) !== 'undefined')
                callback(todo);
        });
    };

    TodoClient.prototype.delete = function(data, callback) {
        var url = '/api/v1/todos/' + data.id + '/';

        var $request = $.ajax({ type: 'DELETE', url: url });

        $request.done(function(result) {
            if ((typeof callback) !== 'undefined')
                callback(data);
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