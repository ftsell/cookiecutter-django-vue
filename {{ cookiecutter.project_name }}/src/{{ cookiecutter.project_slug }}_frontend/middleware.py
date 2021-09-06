from pathlib import Path

from whitenoise.middleware import WhiteNoiseMiddleware


DIST_DIR = Path(__file__).absolute().parent / "{{ cookiecutter.project_slug }}_vue" / "dist"


class FrontendMiddleware(WhiteNoiseMiddleware):
    """
    A middleware which uses whitenoise to efficiently serve the built frontend files.

    It also serves index.html for all unknown urls which is
    `necessary when using the HTML5 History Mode API <https://router.vuejs.org/guide/essentials/history-mode.html>`_.
    """
    def configure_from_settings(self, settings):
        super().configure_from_settings(settings)
        self.static_prefix = "/app/"
        self.static_root = str(DIST_DIR)
        self.autorefresh = False
        self.use_finders = False

    def process_request(self, request):
        result = super().process_request(request)

        if result is None and self.url_is_canonical(request.path_info) and request.path_info.startswith(self.static_prefix):
            result = self.serve(self.files.get("/app/index.html"), request)

        return result


