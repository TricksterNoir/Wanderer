from typing import Dict

class ParticipantFinder:
    def __init__(self, participant_repository) -> None:
        self.__participant_repository = participant_repository

    def find_participants_from_trip(self, trip_id: str) -> Dict:
        try:
            participants = self.__participant_repository.find_participants_from_trip(trip_id)

            participants_infos = []
            for participant in participants:
                participants_infos.append({
                    "id": participant[0],
                    "name": participant[1],
                    "is_confirmed": participant[2],
                    "email": participant[3]
                })

                return {
                    "body": {"participants": participants_infos},
                    "status_code": 200
                }
        except Exception as exception:
            return{
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }