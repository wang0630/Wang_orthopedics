class AnnouncementsOperation {
  constructor(idMapping) {
    this._idMapping = idMapping;
    this.deleteAnnouncement = this.deleteAnnouncement.bind(this);
  }

  async deleteAnnouncement(index) {
    const targetId = this._idMapping[index].id;
    try {
      const url = 'http://127.0.0.1:5000/announcements/deletion/' + targetId;
      console.log(url);
      const res = await axios.delete(url);
      console.log(res);
    } catch(e) {
      console.log(e);
    }
  }
}