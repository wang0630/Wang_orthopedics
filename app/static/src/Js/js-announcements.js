class AnnouncementsOperation {
  constructor(idMapping) {
    this._idMapping = idMapping;
    this.deleteAnnouncement = this.deleteAnnouncement.bind(this);
  }

  deleteAnnouncement(index) {
    console.log(this._idMapping[index]);
  }
}