class AnnouncementsOperation {
  constructor(idMapping, ip) {
    this._idMapping = idMapping;
    this._ip = ip;
    this.deleteAnnouncement = this.deleteAnnouncement.bind(this);
  }

  async deleteAnnouncement(index) {
    if (confirm('確定要刪除這個公告？')) {
      const targetId = this._idMapping[index].id;
        try {
          // const url = this._ip + '/announcements/deletion/' + targetId;
          const url = `${this._ip}/announcement/${targetId}`;
          console.log(url);
          const res = await axios.delete(url);
        } catch(e) {
          console.log(e);
        }
        // Reload the page
        window.location.reload(true);
      }
    }
}
