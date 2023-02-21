from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

from project.models import movie_schema

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        movies = movie_service.get_all(**page_parser.parse_args())
        return movie_schema.dump(movies, many=True)


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        movie_ = movie_service.get_item(movie_id)
        return movie_schema.dump(movie_)
