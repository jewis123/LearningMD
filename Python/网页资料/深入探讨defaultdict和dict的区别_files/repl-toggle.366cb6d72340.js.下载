$(document).ready(function () {
    $('.repl-toggle').click(function (e) {
        e.preventDefault();
        var button = $(this);
        if (!button.data('hidden') || button.data('hidden') === 'yes') {
            button.parent().find('code:has(.gt)').contents().filter(function () {
                return ((this.nodeType == 3) && (this.data.trim().length > 0));
            }).wrap('<span>');

            button.parent().find('.go, .gp, .gt, .gh').hide();
            button.next('pre').find('.gt').nextUntil('.gp, .go').css('visibility', 'hidden');
            button.data('hidden', 'no');
        } else {
            // show the code output
            button.parent().find('.go, .gp, .gt, .gh').show();
            button.next('pre').find('.gt').nextUntil('.gp, .go').css('visibility', 'visible');
            button.data('hidden', 'yes');
        }
    });
});
