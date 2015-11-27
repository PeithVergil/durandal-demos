define([
    'knockout'
], function(ko) {
    function Todo(id, title) {
        // The primary key.
        this.id = id;

        this.title = ko.observable(title);

        // Temporary storage for the title
        // as it's being updated.
        this.draft = ko.observable(title);

        // Has the todo been completed?
        this.done = ko.observable(false);

        // Is the todo beeing updated?
        this.edit = ko.observable(false);
    }

    return Todo;
});