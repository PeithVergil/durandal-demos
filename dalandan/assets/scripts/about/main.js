define(function(require) {
    var ko = require('knockout');

    return {
        welcome: ko.observable('hello, world!'),
    };
});